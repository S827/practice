my_tuple = (1, 'str', 4.5, False)
print(my_tuple[3])
print(type(my_tuple))

tup1 = 1, 'oh', True, 23.1
print(tup1[3])
print(type(tup1))

print(my_tuple.count('int'))

# get the index number of tuple element
ind = tup1.index(23.1)
print(ind)

#loops in tuple
for x in tup1:
    print(x)

#tuples cant be modified
tup1[4] = 5
print(tup1)
