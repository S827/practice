# 2. Python program to interchange first and last elements in a list

l1 = [1, 2, True, 23.1, 'oh']
# x = l1[len(l1)-1]
# # print(x)
# # l1[0] = x
# l1[len(l1)-1] = l1[0]
# l1[0] = x
# print(l1)
def interchange(list):
    x = list[len(list) - 1]
    list[len(list) - 1] = list[0]
    list[0] = x
    return list
print(interchange(l1))