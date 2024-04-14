# 1. What are the Different ways to clear a list in Python

#with clear method
l1 = [1, 2, 'oh']
l1.clear()
print(l1)

# with del keyword
l2 = [2, 3, 4]
del l2[:]
print(l2)

# assigning empty list to the list
l3 = [45]
l3[:] = []
print(l3)

