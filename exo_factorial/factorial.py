
import logging

class ToyMath():

    @staticmethod
    def factorial_at_Speed(factNumber):
        if (type(factNumber) != int):
            return "please enter a number!"
        if factNumber == 0 :
            return 1
        elif (factNumber < 0 ):
            return "please use postive number"
        else :
            return factNumber * ToyMath.factorial_at_Speed(factNumber - 1)


res = ToyMath.factorial_at_Speed("hello")