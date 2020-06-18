import os
import json
from signal import signal, SIGINT
from sys import exit
from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)


DEBUG = True if os.getenv(
    'DEBUG', 'OFF') == 'ON' else False
LED_DEFAULT_VALUE = GPIO.LOW if os.getenv(
    'LED_DEFAULT_VALUE', 'OFF') == 'OFF' else GPIO.HIGH

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
    GPIO.output(value, LED_DEFAULT_VALUE)


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
            GPIO.output(value, GPIO.HIGH)
        else:
            GPIO.output(value, GPIO.LOW)

    return jsonify({"success": True})


@app.route('/game/<romname>', methods=['DELETE'])
def endGame(romname):
    if (DEBUG):
        print("--- Stop " + romname + " ---")
    for key in pinMapping:
        GPIO.output(pinMapping[key], LED_DEFAULT_VALUE)
    return jsonify({"success": True})


def exitHandler():
    GPIO.cleanup()
    if (DEBUG):
        print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0')
    signal(SIGINT, exitHandler)
