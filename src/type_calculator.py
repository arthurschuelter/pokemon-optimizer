# --------------------------------------------------------
from enum import Enum

# --------------------------------------------------------


class Type(Enum):
    NORMAL = 0
    GRASS = 1
    WATER = 2
    FIRE = 3


class TypeCalculator:
    def __init__(self):
        print("Hello from TypeCalculator")

    def print(self):
        print("Hello again from TypeCalculator")
