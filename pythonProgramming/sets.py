# declare set
set_a = {1, 2, 3, 4, 5}
print(set_a)

# duplication not allowed in set
set_b = {1, 2, 3, 3, 4, 5, 5, 4}
print(set_b)

#add item to set with set.add(value)
set_a.add(6)
print(set_a)

#remove item froms set with set.remove(value) and set.discard(value)
set_a.remove(2)
print(set_a)
set_a.discard(6)
print(set_a)

#set operations- union, set.union(set1)OR set1 | set2
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 5, 6, 9}
print(set1.union(set2))
print(set1 | set2)

#SET Operations- Intersection: set1.intersection(set2) OR set1 & set2
print(set1.intersection(set2))
print(set1 & set2)

# SET Operations-- difference: set1.difference(set2) OR set1 - set2
print(set1.difference(set2))
print(set1 - set2)
print(set2 - set1)

# SET Op: symmetrical_difference: set1.symmetrical_difference(set2) OR set1 ^ set2
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
print(set2 ^ set1)
#set is not subscriptable, which means that set is not sequence and unordered
