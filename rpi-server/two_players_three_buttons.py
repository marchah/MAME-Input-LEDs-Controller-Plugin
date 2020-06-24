import RPi.GPIO as GPIO

from utils import initLEDs, setLEDsValue, resetLEDsValue


class TwoPlayersThreeButtons:
    def __init__(self, ledDefaultValue):
        self.ledDefaultValue = ledDefaultValue
        self.playerOnePins = {
            'B_0': 2,
            'B_1': 3,
            'B_2': 4,
        }
        self.playerTwoPins = {
            'B_0': 14,
            'B_1': 15,
            'B_2': 18,
        }

        GPIO.setmode(GPIO.BCM)
        initLEDs(self.playerOnePins, ledDefaultValue)
        initLEDs(self.playerTwoPins, ledDefaultValue)

    def setLEDs(self, inputs, nbPlayers):
        setLEDsValue(self.playerOnePins, inputs)

        if (nbPlayers >= 2):
            setLEDsValue(self.playerTwoPins, inputs)

    def resetLEDs(self):
        resetLEDsValue(self.playerOnePins, self.ledDefaultValue)
        resetLEDsValue(self.playerTwoPins, self.ledDefaultValue)


def createTwoPlayersThreeButtons(ledDefaultValue):
    return TwoPlayersThreeButtons(ledDefaultValue)
