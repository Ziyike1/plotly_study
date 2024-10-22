from random import randint

class Die:
    """表示一个骰子的类"""

    def __init__(self, sides=6):
        """骰子默认为六面"""
        self.sides = sides

    def roll(self):
        """返回一个介于1和骰子面数之间的随机值"""
        return randint(1, self.sides)