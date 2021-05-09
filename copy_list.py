from debug_log import p

l1 = [1, 2, 3]
p(l1)

l2 = l1.copy()
l2.append(4)

p(l2)
p(l1)

l3 = l1.copy() + [5]

p(l3)

p(l1)

l4 = l1 + [5]

p(l4)
p(l1)

"""
l1 :  [1, 2, 3]
l2 :  [1, 2, 3, 4]
l1 :  [1, 2, 3]
l3 :  [1, 2, 3, 5]
l1 :  [1, 2, 3]
l4 :  [1, 2, 3, 5]
l1 :  [1, 2, 3]
"""