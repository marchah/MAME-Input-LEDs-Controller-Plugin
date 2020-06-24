import RPi.GPIO as GPIO

from utils import initLEDs, setLEDsValue, resetLEDsValue


class OnePlayerEightButtons:
    def __init__(self, ledDefaultValue):
        self.ledDefaultValue = ledDefaultValue
        self.playerOnePins = {
            'B_0': 2,
            'B_1': 3,
            'B_2': 4,
            'B_3': 17,
            'B_4': 27,
            'B_5': 22,
            'B_6': 10,
            'B_7': 9
        }

        GPIO.setmode(GPIO.BCM)
        initLEDs(self.playerOnePins, ledDefaultValue)

    def setLEDs(self, inputs, nbPlayers):
        setLEDsValue(self.playerOnePins, inputs)

    def resetLEDs(self):
        resetLEDsValue(self.playerOnePins, self.ledDefaultValue)


def createOnePlayerEightButtons(ledDefaultValue):
    return OnePlayerEightButtons(ledDefaultValue)
