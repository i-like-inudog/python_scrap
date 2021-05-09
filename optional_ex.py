from typing import Optional

from debug_log import p

class Value:
    def __init__(self, value: int):
        self.value = value

    def test(self, maybe_value: Optional[int]) -> Optional[int]:
        return maybe_value

val = Value(1)

opt_int: int = 1

opt_val = val.test(opt_int)

p(opt_val)