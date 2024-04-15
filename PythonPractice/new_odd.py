# we need to interate for few times, we wil use for loop
# pause the program for specified number of seconds, sleep function from time
# module can do this
# generate a random number bw 2 provided values, randint function from random
# module can be used

from datetime import datetime
import time
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37,
        39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute seeams a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)
