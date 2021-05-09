from parent.parent_module1 import show

def show_child():
    print("child!!!!!")
    show()

if __name__ == '__main__':
    show_child()

"""
path_to/scrap $ python3 parent/child/child_module.py

ImportError: attempted relative import with no known parent package


path_to/scrap $ python3 -m parent.child.child_module
child!!!!!
Parent!!
""" 