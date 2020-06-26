import os
import json
from signal import signal, SIGINT
from sys import exit
from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)


DEBUG = True if os.getenv(
    'DEBUG', 'OFF') == 'ON' else False
LED_DEFAULT_VALUE = os.getenv('LED_DEFAULT_VALUE', 'ON')
MY_RELAY_IS_REVERSE = True if os.getenv(
    'MY_RELAY_IS_REVERSE', 'TRUE') == 'TRUE' else False

relayOnState = GPIO.HIGH
relayOffState = GPIO.LOW

if (MY_RELAY_IS_REVERSE):
    relayOnState = GPIO.LOW
    relayOffState = GPIO.HIGH

ledDefaultValue = relayOnState if LED_DEFAULT_VALUE == 'ON' else relayOffState

pinMapping = {
    'B_0': 2,
    'B_1': 3,
    'B_2': 4,
    'B_3': 17,
    'B_4': 27,
    'B_5': 22,
    'B_6': 10,
    'B_7': 9
}

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
for key in pinMapping:
    value = pinMapping[key]
    GPIO.setup(value, GPIO.OUT)  # GPIO Assign mode
    GPIO.output(value, ledDefaultValue)


@app.route('/debug', methods=['POST'])
def debug():
    print("-- DEBUG --")
    print(request.json)
    return jsonify({"success": True})


@app.route('/game/<romname>', methods=['POST'])
def playGame(romname):
    if (DEBUG):
        print("--- Playing " + romname + " ---")
    content = request.json

    # should check if inputs is array of string too
    if not content["inputs"]:
        return jsonify({"success": False, "message": "Missing inputs"})

    for key in pinMapping:
        value = pinMapping[key]
        if key in content["inputs"]:
            GPIO.output(value, relayOnState)
        else:
            GPIO.output(value, relayOffState)

    return jsonify({"success": True})


@app.route('/game/<romname>', methods=['DELETE'])
def endGame(romname):
    if (DEBUG):
        print("--- Stop " + romname + " ---")
    for key in pinMapping:
        GPIO.output(pinMapping[key], ledDefaultValue)
    return jsonify({"success": True})


def exitHandler():
    GPIO.cleanup()
    if (DEBUG):
        print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0')
    signal(SIGINT, exitHandler)
