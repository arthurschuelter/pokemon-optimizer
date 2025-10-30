# --------------------------------------------------------
from enum import Enum


# --------------------------------------------------------
class Type(Enum):
    NORMAL = 0
    GRASS = 1
    WATER = 2
    FIRE = 3


this_type = Type.NORMAL
print(this_type.name, this_type.value)
