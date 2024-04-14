l1 = [1, 2, 3, 4, 5]
print(l1[3])
l2 = ['A', 'B', 'C']

l3 = ['Hello', 1, True, 12.34]

l4 = [1, [2, 3, 4], 5, 6]

print(*l1)
print(*l2)
print(*l3)
print(*l4)

print(l1, sep=" ")
# INSERTING ITEM INTO LIST 1.insert(index, value) 2.append(value) 
# 3.extend(list)
l1.insert(len(l1), 22)
print(*l1)
l1.append(33)
print(l1)
l1.extend([44, 55, 66, 77])
print(*l1)

#REMOVE ITEM FROM LIST
# 1. pop(index) 2.del

l1.pop(len(l1) - 1)
print(*l1)

del l1[len(l1) - 1]
print(*l1)

#LOOP in list
for x in l1:
    print("value: ", x)
