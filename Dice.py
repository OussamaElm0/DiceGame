import random as rd

class Dice:
    @staticmethod
    def play():
        number1 = rd.randint(1,6)
        number2 = rd.randint(1,6)
        return number1, number2
