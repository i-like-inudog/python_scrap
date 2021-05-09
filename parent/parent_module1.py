from parent.child.child_module_2 import show_child2

def show():
    print("Parent!!")

if __name__ == '__main__':
    show()
    show_child2()

"""
1. 
from parent.child.child_module_2 import show_child2

path_to/scrap $ python3 parent/parent_module1.py

ImportError: attempted relative import with no known parent package

2. 
from parent.child.child_module_2 import show_child2

path_to/scrap $ python3 -m parent.parent_module1

Parent!!
child22222222222

3. 
from child.child_module_2 import show_child2

path_to/scrap $ python3 parent/parent_module1.py
Parent!!
child22222222222

"""