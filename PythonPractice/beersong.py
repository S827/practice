import time, random

# assign the value "bottles" a string to the variable word
word = "bottles"

# start a for loop to iterate over 99 times using range function with start,
# stop and step arguments
for beer_num in range(99, 0, -1):
    # display beer_num, word, which is 99 bottles of beer on the wall
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    # if beer_num is 1 we need to print the string
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    # else we decrease the beer_num by 1 and assign it to new_num
    else:
        new_num = beer_num - 1
        # and check if new_num is 1, if yes, word should be bottle not bottles gramatically
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
    print()
    time.sleep(random.randint(1, 5))

