# 인데스 슬라이싱
# animals = ['dog', 'dog','cat', 'bird', 'fish']
#
# # list[inclusive_start=0 : exclusive_end=len(list)] -> list
# print(animals)
# print(animals[0:3])
# print(animals[1:4])
# print(animals[:2])
# print(animals[2:])
#
# # list[inclusive_start=0 : exclusive_end=len(list) : step=1] -> list
# food = ['noodle', 'meat', 'bread', 'chicken']
# print(food[:3:2])
# print(food[2::2])
#
# # 역순 출력
# print(food[::-1])
#
# number_list = list(range(1, 11))
# print(number_list)
#
# # [1, 3, 5, 7, 9]
# # [6, 5, 4, 3, 2]
# # [2, 4, 6]
# # [2, 3, 4, 5, 6, 7]
#
#
# #1.
# print(number_list[::2])
#
# #2
# print(number_list[5:0:-1])
#
# #3
# print(number_list[1:6:2])
#
# #
# print(number_list[1:7:1])
#
#
#
# animals = ['dog','dog', 'cat', 'bird']
# zoo = ['panda', 'giraffe']
#
# animals[1:2] = zoo
# print(animals)
#
# animals.insert(animals.index('dog') + 1, 'giraffe')
# print(animals)
#
# animals.insert(animals.index('cat') + 1, zoo)


# 슬라이싱, insert, del 를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']
# animals = ['dog', 'dog', 'cat', 'bird']
animals = ['dog', 'hamster', 'fish', 'dog', 'whale', 'bird']
print(animals)

del(animals[1:3])
animals[2] = 'cat'
print(animals)