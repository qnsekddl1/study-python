# 문자열끼리만 연결(+)이 가능하다
# data = 3
# print('안' + str(data))
# name = input("이름: ")
# # print(name + '님 환영합니다')
# formatting = f'{name}님 환영합니다.'
# print(formatting)

# 제 이름은 ???, 키는 ???cm 입니다

# name = input("이름: ")
# height = input("키: ")
# formatting = f'제 이름은 {name}, 제 키는 {height}cm 입니다.'
# print(formatting)

# 두 정수를 입렵 받은 후 곱셈 결과 출력

# number1 = input("첫번째 정수: ")
# number2 = input("두번째 정수: ")
# number3 = int(number1) * int(number2)
# formatting = f'{number1} * {number2} = {number3}'
# print(formatting)

# message1 = '첫번째 정수: '
# message2 = '두번째 정수: '
# number1 = int(input(message1))
# number2 = int(input(message2))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
# print(formatting)

# map(각각 어떻게 바꿀 것인가,[])
# message = '두 정수를 입력하세요'
# example_message = '예)1, 3'
# number1, number2 = map(int, input(message + '\n' + example_message + '\n').split(', '))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
#
# print(formatting)


# 현재 시간을 입력하고 시와 분으로 분리하여 출력
# 핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
# 이름과 나이를 한번에 입력 받은 뒤 "???님의 나의는 ???살' 형식으로 출력
# 3개의 정수를 입력 받은 뒤 덧셈 결과 출력


#1
# message = '현재 시간을 입력하세요'
# example_message = '예)18시 30분'
# number1, number2 = input(message + '\n' + example_message + '\n').split(' ')
# formatting = f'{number1}\n{number2}'
# print(formatting)
#
# #2
message = '휴대폰 번호를 - 포함하여 입력 해주세요'
example_message = '예) 010-1234-5678'
number1, number2, number3 = input(message + '\n' + example_message + '\n').split('-')
formatting = f'{number1}\n{number2}\n{number3}'
print(formatting)
#
# #3
# message = '이름과 나이를 입력해주세요'
# example_message = '예)이기영, 30'
# number1, number2 = input(message + '\n' + example_message + '\n').split(', ')
# formatting = f'{number1}님의 나이는 {number2}살 입니다.'
# print(formatting)
#
# # 4
# message = '세 정수를 입력하세요'
# example_message = '예)1/3/5'
# number1, number2, number3 = map(int, input(message + '\n' + example_message + '\n').split('/'))
# result = number1 + number2 + number3
# formatting = f'{result}'
# print(formatting)


# 4개의 정수를 입력 받아 총 곱을 구해라

# message = '네 정수를 입력하세요'
# example_message = 'ex) 1/2/3/4'
# number1, number2, number3, number4 = map(int, input(message + '\n' + example_message + '\n').split('/'))
# result = number1 * number2 * number3 * number4
# formatting = f'{result}'
# print(formatting)
