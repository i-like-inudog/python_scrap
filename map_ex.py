from debug_log import p

class Cover:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f'Cover({self.value})'

l = [1, 2, 3]

mapped_l = list(map(Cover, l))

p(mapped_l)


## multi paramater

class Cover2:
    def __init__(self, value: int, value2: str):
        self.value = value
        self.value2 = value2

    def __repr__(self):
        return f'Cover2({self.value}, {self.value2})'

l2 = [1, 2, 3]

mapped_l2 = list(map(Cover2, l2, l2))

p(mapped_l2)


## nest list

ll = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

mapped_ll = list(map(lambda l: list(map(Cover, l)), ll))

p(mapped_ll)