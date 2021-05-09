from dataclasses import dataclass
from enum import Enum, auto

from debug_log import p

# dataclassとenumは共存できない？どちらにせよ複雑になりそうだからあまりよくなさそうだが
@dataclass
class EnumLike(Enum):
    EMPTY = auto()
    val: int = 0

    

# instance = EnumLike(1)

enum_like_value = EnumLike.EMPTY

# p(instance)
p(enum_like_value)
