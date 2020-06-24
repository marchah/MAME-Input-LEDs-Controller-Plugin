import os
import json
from signal import signal, SIGINT
from sys import exit
from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

from one_player_eight_buttons import createOnePlayerEightButtons
from two_players_three_buttons import createTwoPlayersThreeButtons

app = Flask(__name__)

ONE_PLAYER_EIGHT_BUTTONS = 'ONE_PLAYER_EIGHT_BUTTONS'
TWO_PLAYERS_THREE_BUTTONS = 'TWO_PLAYERS_THREE_BUTTONS'


DEBUG = True if os.getenv(
    'DEBUG', 'OFF') == 'ON' else False
LED_DEFAULT_VALUE = GPIO.LOW if os.getenv(
    'LED_DEFAULT_VALUE', 'OFF') == 'OFF' else GPIO.HIGH
VERSION = os.getenv('VERSION', TWO_PLAYERS_THREE_BUTTONS)

versions = {
    ONE_PLAYER_EIGHT_BUTTONS: createOnePlayerEightButtons,
    TWO_PLAYERS_THREE_BUTTONS: createTwoPlayersThreeButtons,
}

inputController = versions[VERSION](LED_DEFAULT_VALUE)


@app.route('/debug', methods=['POST'])
def debug():
    print("-- DEBUG --")
    print(request.json)
    return jsonify({"success": True})


@app.route('/game/<romname>', methods=['POST'])
def playGame(romname):
    if (DEBUG):
        print("--- Playing " + romname + " ---")
    inputs = request.json["inputs"]
    nbPlayers = request.json["nbPlayers"]

    # should check if inputs is array of string too
    if not inputs:
        return jsonify({"success": False, "message": "Missing inputs"})

    if not nbPlayers:
        return jsonify({"success": False, "message": "Missing nbPlayers"})

    if not nbPlayers.is_integer():
        return jsonify({"success": False, "message": "nbPlayers should be an integer"})

    inputController.setLEDs(inputs, nbPlayers)

    return jsonify({"success": True})


@ app.route('/game/<romname>', methods=['DELETE'])
def endGame(romname):
    if (DEBUG):
        print("--- Stop " + romname + " ---")
    inputController.resetLEDs()
    return jsonify({"success": True})


def exitHandler():
    GPIO.cleanup()
    if (DEBUG):
        print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0')
    signal(SIGINT, exitHandler)
