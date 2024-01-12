# number = 15
#
# if number % 3 == 0:
#     print(f'{number}는 3의 배수입니다.')
# if number % 5 == 0:
#     print(f'{number}는 5의 배수입니다.')


#number가 양수인지, 음수인지, 0인지 검사

# number = 1
# if number > 0:
#     print(f'{number}은(는) 양수입니다.')
# elif number < 0:
#     print(f'{number}은(는) 음수입니다.')
# elif number == 0:
#     print(f'{number}은(는) 0입니다.')

# number = 0
# positive_condition = number > 0
# negative_condition = number < 0
#
# if positive_condition:
#     print(f'{number} 은(는) 양수 입니다')
# elif negative_condition:
#         print(f'{number} 은(는) 음수 입니다')
# else:
#     print(f'{number} 입니다')

# message = '나이: '
# age = int(input(message))
# adult_condition = age > 19
#
# if adult_condition:ㄴ
# else:
#     print(f'{age}살은 미성년자 입니다')

# message = '나이: '
# age = int(input(message))
# condition = 0 < age < 20
# error_condition = age <= 0
#
# if condition:
#     print('미성년자입니다.')
# elif error_condition:
#     print('잘못 입력하셨습니다')
# else:
#     print('성인입니다')


# 두 정수를 입력 받은 후 대소 비교

# message1 = '첫 번째 정수: '
# message2 = '두 번째 정수: '
# number1 = int(input(message1))
# number2 = int(input(message2))

# num1_condition = number1 > number2
# num2_condition = number2 > number1
# tie_condition = number1 == number2
# 선언할 때 넣을 값을 모를 경우 초기값을 넣어준다.
# 정수: 0
# 실수: 0.0
# 문자열; '' 또는 ""
# 불린: False

# result_message = ''

# 일괄처리란,
# 각 분기별로 결과를 처리하지 않고,
# 모든 분기

# if num1_condition:
#     result_message = f'{number1}이(가) {number2} 보다 큽니다.'
# elif num2_condition:
#     result_message = f'{number2}이(가) {number1} 보다 큽니다.'
# else:
#     result_message = '두 수가 같습니다.'
# print(result_message)
#
# print(in range10):


# 사용자에게 아래의 메뉴를 출력하고 번호를 입력받는다.

# 1. 빨간색
# 2. 검은색
# 3. 노란색
# 4. 흰색

# 사용자가 입력한 번호의 색상을 영어로 출력한다.
title = "색상은 골라주세요!\n"
menu = "1. 빨간색\n" \
       "2. 검은색\n" \
       "3. 노란색\n" \
       "4. 흰색\n"

choice = int(input(title + menu))
choice1, choice2, choice3, choice4 = choice == 1, choice == 2, choice == 3, choice == 4
color1, color2, color3, color4 = "red", "black", "yellow", "white"
result = None

if choice1:
    result = color1
elif choice2:
    result = color2
elif choice3:
    result = color3
elif choice4:
    result = color4

print(result)


