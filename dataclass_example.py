from debug_log import p

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    desc: str

    def show(self):
        print(f'title: {self.title}. desc: {self.desc}')

book1 = Book(title='ttttttttttt', desc='this is descripition')

book1.show()

## Noneをコンストラクタに代入できるか？
none_title_book = Book(title=None, desc='this is desc.')


## dictを使ってインスタンス化できるか？
book_dict = {'title': 'This is title from dict', 'desc': 'from dict'}

# できない
# book2 = Book(book_dict)

# p(book2)


print('--------- fronze=True ----------')

# frozen=Trueの場合のインスタンスの同一性の検証
@dataclass(frozen=True)
class Desk:
    height: int
    width: int

desk1 = Desk(50, 100)
desk2 = Desk(50, 100)

is_same_desk = desk1 == desk2

# eqはデフォルトでTrueなので、Trueになるはず
p(is_same_desk)

desk_set = {desk1}

p(desk_set)

# frozen=Trueにすることで__hash__が実装されるはず
desk_set.add(desk2)

# 値の同一性で検証されれば追加はできないはず
p(desk_set)