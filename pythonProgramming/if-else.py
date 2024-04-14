# check if the dessert "Churros" is in the list and if it is, print a single 
# statement. 
favorites = ["ice cream", "kaju barfi", "gajar halwa", "gulab jamun", "paan"]
# for dessert in favorites:
#     if dessert == 'paan':
#         print("Yes! One of my fav dessert is ", dessert)

# # if dessert is not in the list
# for dessert in favorites:
#     if dessert == 'kaan':
#         print("Yes! One of my fav dessert is ", dessert)
#     else:
#         print("Dessert is not in the list")

# use of break statement to avoid printing unnecessary lines
# for dessert in favorites:
#     if dessert == 'paan':
#         print("Yes! One of my fav dessert is ", dessert)
#         break
#     else:
#         print("Dessert is not in the list")

# use of continue statement
for des in favorites:
    if des == 'paan':  # this dessert will not be printed due to continue
        continue
    print("Other desserts I like are ", des)

# use of pass stattement
for des in favorites:
    if des == 'paan':
        pass
    print("Other desserts I like are ", des)