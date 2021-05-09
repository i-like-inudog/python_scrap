from __future__ import annotations
# python3.9時点だと、このimportしないと -> Testの部分で落ちる

from debug_log import p


class Test:
    def __init__(self, value: str):
        self.value = value

    def from_str(self, value: str) -> Test:
        return Test(value + '!!!!!!!!!!!!!!!!1')

test = Test('value')

p(test.from_str('this is test'))
