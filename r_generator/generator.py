import os
import psutil

# data_list = [i ** 2 for i in range(100)]
# print(data_list)
#
# data_list = (i ** 2 for i in range(100))
# print(next(data_list))



def increase(number : int = 1):
    while True:
        number += 1
        yield number

result = increase()
while True:
    data = input("y/n >> ")
    if data == "y":
        print(next(result))
    else:
        break