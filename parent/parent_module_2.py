from parent.child.child_module import show_child

def show():
    show_child()

if __name__ == '__main__':
    show_child()

"""
呼び出してるモジュールの中で、さらに他モジュール呼び出しに相対インポートなどを用いていると、結構厄介になりそう。
基本的には絶対importの方が良さそう
"""