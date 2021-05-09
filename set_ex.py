from debug_log import p



"""
setで、独自クラスのインスタンスを扱う際に同一条件がどのように判定されるのかの試行

TL;DR 
- https://www.yoheim.net/blog.php?q=20171001
- https://docs.python.org/ja/3/reference/datamodel.html#object.__hash__
"""

class Item:
    def __init__(self, value: int):
        self.value = value

item_1 = Item(1)
item_2 = Item(1)

# valueが同じでも違うオブジェクトとして判定される（これは当たり前）
is_same_item = item_1 == item_2

p(is_same_item) # False

item_set = {item_1}

p(item_set)

# 同じオブジェクトは追加できない
item_set.add(item_1)

p(item_set)

# 違うオブジェクトなので追加できる
item_set.add(item_2)

p(item_set)


class Obj:
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Obj):
            return False
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

obj_1 = Obj(1)
obj_2 = Obj(1)

# eqを定義したことで、valueが同じならオブジェクトの比較をするときにはTrueになる
is_same_obj = obj_1 == obj_2

p(is_same_obj)

# eqだけ定義して、__hash__を定義しないとここでエラー
# TypeError: unhashable type: 'Obj'
obj_set = {obj_1}

p(obj_set)

# 同じオブジェクトは追加できない
obj_set.add(obj_1)

p(obj_set)

# 違うオブジェクトだが、eqとhashの実装からvalueの条件で判定されるため追加できない
p(id(obj_1))
p(id(obj_2))

obj_set.add(obj_2)

# 1つしか値がないから追加できていなことが確認できる
p(obj_set)

