#1
# email을 입렵 받고 아이디와 도메인을 각각 분리하여 출력한다.

# message = '이메일을 입력 해주세요'
# example_message = '예) kssudgktpdy@naver.com'
# id, domain = input(message + '\n' + example_message + '\n') .split('@')
# formatting = f'아이디는 {id} 이고, 도메인은 {domain} 입니다'
#
# print(formatting)

#2
# 첫 번째 값으로 야드를 입력받고, 두 번쨰 값으로 인치를 입력받아서
# 각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.

# message = '야드와 인치를 각각 순서대로 입력해주세요'
# example_message = '11/12'
#
# yard, inch = input(message + '\n' + example_message + '\n').split('/')
# formatting = f'{float(yard) * 91.44}cm, {float(inch) * 2.45}cm'
# print(formatting)

yard_message = 'yard: '
inch_message = 'inch: '

yard = float(input(yard_message))
inch = float(input(inch_message))

yard_to_cm = round(yard * 91.44, 2)
inch_to_cm = round(inch * 2.45, 2)

yard_formatting = f'{yard} yard는 {yard_to_cm}cm'
inch_formatting = f'{inch} inch는 {inch_to_cm}cm'

print(yard_formatting, inch_formatting, sep='\n')

#     1yd: 91.44cm
#     1in: 2.45cm
#     예)
#         yard 입력: 10
#         inch 입력: 10
#
#         10 yard는 914.4cm
#         10 inch는 25.4cm

# round(값, 원하는 자리수): 소수점이 맞춰진 결과값
