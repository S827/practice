# nested loops, bellow ex prints 2D array of zeroes
# for i in range(10):
#     #inner loop
#     for j in range(10):
#         print(0, end=" ")
#     print()

# print single row of zeroes
# for i in range(1):  #outer loop will run only once
#     for j in range(10): #inner loop will run 10 times
#         print(0, end=" ")
import time
start_time = time.time()

for i in range(1000):
    for j in range(1000):
        print(0, end=" ")
    print()
print(round(time.time() - start_time, 2))
