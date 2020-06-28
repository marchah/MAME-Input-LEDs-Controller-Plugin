import RPi.GPIO as GPIO

from utils import initLEDs, setLEDsValue, resetLEDsValue


class TwoPlayersEightButtonsComplex:
    def __init__(self, ledDefaultValue, relayOnState, relayOffState):
        self.ledDefaultValue = ledDefaultValue
        self.relayOnState = relayOnState
        self.relayOffState = relayOffState
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
        self.playerTwoPins = {
            'ALL': 14
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


def createTwoPlayersEightButtonsComplex(ledDefaultValue, relayOnState, relayOffState):
    return TwoPlayersEightButtonsComplex(ledDefaultValue, relayOnState, relayOffState)
