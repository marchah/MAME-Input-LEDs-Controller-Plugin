import RPi.GPIO as GPIO

from utils import initLEDs, setLEDsValue, resetLEDsValue


class TwoPlayersThreeButtons:
    def __init__(self, ledDefaultValue, relayOnState, relayOffState):
        self.ledDefaultValue = ledDefaultValue
        self.relayOnState = relayOnState
        self.relayOffState = relayOffState
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
        setLEDsValue(self.playerOnePins, inputs,
                     self.relayOnState, self.relayOffState)

        if (nbPlayers >= 2):
            setLEDsValue(self.playerTwoPins, inputs,
                         self.relayOnState, self.relayOffState)

    def resetLEDs(self):
        resetLEDsValue(self.playerOnePins, self.ledDefaultValue)
        resetLEDsValue(self.playerTwoPins, self.ledDefaultValue)


def createTwoPlayersThreeButtons(ledDefaultValue, relayOnState, relayOffState):
    return TwoPlayersThreeButtons(ledDefaultValue, relayOnState, relayOffState)
