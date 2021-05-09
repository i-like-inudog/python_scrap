from debug_log import p

class First:
    def __init__(self, value: int):
        self.value = value

class Second:
    def __init__(self, value: First):
        self.value = value
# 正しい順序
first = First(1)
p(first)
second = Second(first)
p(second)

class Third:
    def __init__(self, value: Fourth):
        self.value = value

class Fourth:
    def __init__(self, value: int):
        self.value = value

# 実行順序逆にしないと通らない
fourth = Fourth(1)
p(fourth)
third = Third(fourth)
p(third)
