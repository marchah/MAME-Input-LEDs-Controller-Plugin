import RPi.GPIO as GPIO


def initLEDs(pins, ledDefaultValue):
    for key in pins:
        value = pins[key]
        GPIO.setup(value, GPIO.OUT)  # GPIO Assign mode
        GPIO.output(value, ledDefaultValue)


def setLEDsValue(pins, inputs, relayOnState, relayOffState):
    for key in pins:
        value = pins[key]
        if key in inputs:
            GPIO.output(value, relayOnState)
        else:
            GPIO.output(value, relayOffState)


def resetLEDsValue(pins, ledDefaultValue):
    for key in pins:
        GPIO.output(pins[key], ledDefaultValue)
