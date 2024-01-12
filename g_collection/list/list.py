# # animals = ["dog", "cat", "bird", "fish"]
# # # print(animals)
# # # print(type(animals))
# #
# # # 인덱스로 접근
# # print(animals[1])
# # print(animals[2])
# #
# # # 음수 인덱스 가능(가장 마지막 순서대로 앞으로 이동한다)
# # print(animals[-1])
# # print(animals[-2])
# #
# # # len()
# # print(len(animals))
# #
# # # append()
# # animals.append("hamster")
# # print(len(animals))
# # print(animals)
# # animals.append("cat")
# # print(animals)
# #
# # # insert
# # animals.insert(1, "dog")
# # print(animals)
# #
# # # remove
# # animals.remove('dog')
# # print(animals)
# #
# # #del()
# # del(animals[0])
# # print(animals)
# #
# # #clear
# # # animals.clear()
# # # print(animals)
# #
# # # index()
# # print(animals.index('bird'))
# # # print(animals.index('tiger'))
# #
# # # 수정
# # # animals[animals.index('bird')] = 'lion'
# # # print(animals)
# # index = animals.index('bird')
# # animals[index] = 'lion'
# # print(animals)
# #
# # # 그 외
# # # animals = ["dog", "cat", "bird", "fish"]
# # # print(animals * 2)
# # #
# # # print("dog" in animals)
# # # print("tiger" in animals)
# # #
# # # for animal in animals:
# # #     print(animal)
#
# # 실습
# # 1~90까지 list에 담고 출력
# # 1~100까지 중 짝수만 list에 담고 출력
# # 1~10까지 list에 담은 후 짝수만 출력
# # 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
#
# # 1. 1~90까지 list에 담고 출력
# # number1 = list(range(1, 91, 1))
# # print(number1)
#
# number_list = [] * 90
# for i in range(len(number_list)):
#     number_list[i] = (i)
# print(number_list)
#
# #2. 1~100까지 중 짝수만 list에 담고 출력
# # number2 = list(range(2, 101, 2))
# # print(number2)
#
# number_list2 = [] * 50
# for i in range(len(number_list)):
#     number_list2[i] = (i + 1) * 2
# print(number_list2)
# #3. 1~10까지 list에 담은 후 짝수만 출력
#
# number_list3 = []
# for i in range(10):
#     number_list3.append(i + 1)
# for i in range(len(number_list3)):
#     if number_list3[i] % 2 == 0:
#         print(number_list3)
#
# #4. 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
# member = ["철수", "영희", "지훈", "은영"]
# member[1] = "수진"
# del(member[3])
# print(member)
# #
# #5
# # price = ["189,000 원"]
# # print(price)
# # price[0] = "189000"
# # print(price)

# list 안에 list
numer_list = [[1, 3, 5],[2, 4, 6]]
# print(numer_list[0][0])
# lenght = len(numer_list) * len(numer_list[0])
#
# for i in range(lenght):
#     print(numer_list[i // 3][i % 3])

for i in range(len(numer_list)):
    for j in range(len(numer_list[i])):
        print(numer_list[i][j])