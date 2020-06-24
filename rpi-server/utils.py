import RPi.GPIO as GPIO


def initLEDs(pins, ledDefaultValue):
    for key in pins:
        value = pins[key]
        GPIO.setup(value, GPIO.OUT)  # GPIO Assign mode
        GPIO.output(value, ledDefaultValue)


def setLEDsValue(pins, inputs):
    for key in pins:
        value = pins[key]
        if key in inputs:
            GPIO.output(value, GPIO.HIGH)
        else:
            GPIO.output(value, GPIO.LOW)


def resetLEDsValue(pins, ledDefaultValue):
    for key in pins:
        GPIO.output(pins[key], ledDefaultValue)
