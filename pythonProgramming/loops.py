favorites = ["ice cream", "kaju barfi", "gajar halwa", "gulab jamun", "paan"]

for item in favorites:
    print("I like this dessert ", item)

count = 0
while count < len(favorites):
    print("I like ", favorites[count])
    count += 1
for idx, item in enumerate(favorites):
    print(idx, item)