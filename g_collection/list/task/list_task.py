# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

title = "또와 과일"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        # 사용자에게 상품명과 가격을 동시에 입력받는다(구분점은 공백문자).
        new_name, new_price = input(append_message).split()
        # 입력한 상품명이 기존 상품과 중복되지 없다면,
        if new_name not in name_list:
            # 이름 list에 추가
            name_list.append(new_name)
            # 가격 list에 추가
            price_list.append(int(new_price))
            # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 skip
            continue
        else:
            # 입력한 상품명이 기존 상품과 중복되었다면,
            # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = append_error_message

    # 수정
    elif choice == 2:
        # 사용자에게 새로운 상품명과 새로운 가격을 입력 받는다
        name = input(search_name_message_for_update)
        if name in name_list:
            new_name, new_price = input(update_message).split()
            # 만약, 새로운 상품명이 리스트에 없다면,
            if new_name not in name_list:
                index = name_list.index(name)
                # 새로운 상품명과 가격을 리스트에 추가한다
                name_list[index], price_list[index] = new_name, new_price
                # 위의 과정이 성공하였으므로 바로 다음 과정 진행
                continue
            #만약 실패한다면,
            else:
                # 에러 메세지를 표출한다
                result_message = update_error_message2
        else:
            # 에러 메세지를 표출한다
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 사용자에게 삭제할 상품명을 입력 받는다
        name = input(delete_message)
        # 상품명이 리스트에 있다면,
        if name in name_list:
            index = name_list.index(name)
            #가격을 먼저 지우고, 상품명을 지운다
            del name_list[index]
            del price_list[index]
            # 위의 과정이 성공하였으므로 바로 다음 과정 진행
            continue

        else:
            # 에러 메세지를 표출한다
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            # 검색할 상품명을 입력 받는다
            name = input(search_name_message)
            # 만약, 입력한 상품명이 리스트에 있다면
            if name in name_list:
                index = name_list.index(name)
                # 상품명과 가격을 표출 한다
                print(f'{name_list[index]}, {price_list[index]}')
                # 위의 과정이 성공하였으므로 바로 다음 과정 진행
                continue

            else:
                # 에러 메세지를 표출한다
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            # 검색할 상품의 가격을 입력 받는다
            price = int(input(search_price_message))
            # 가격의 오차를 -50%
            min = price * 0.5
            # 가격의 오차를 +50%
            max = price * 1.5
            result_index = [price_list.index(i) for i in [price for price in price_list if min <= price <= max]]
            # 만약, 입렵 받은 상품의 가격이 오차범위 내에 있다면
            if len(result_index) != 0:
                for i in result_index:
                    # 상품명과 가격을 표출한다
                    print(f'{name_list[i]}, {price_list[i]}')
                    # 위의 과정이 성공하였으므로 바로 다음 과정 진행
                    continue

            else:
                # 에러 메세지를 표출한다
                result_message = search_error_message
    # 목록
    elif choice == 5:
        # 목록에 아무런 상품이 없다면
        if len(name_list) == 0:
            # 아무런 상품이 없다고 표출 한다
            result_message = no_item_message
        else:
            #만약, 상품이 있다면
            for i in range(len(name_list)):
                # 상품명과 가격을 표출 한다
                print(f'{name_list[i]}, {price_list[i]}')
                # 위의 과정이 성공하였으므로 바로 다음 과정 진행
                continue

    # 나가기
    elif choice == 6:
        # 6번을 입력 하면 프로그램 종료
        break

    # 그 외
    else:
        # 위의 과정 중 에러 메세지가 표출 하여야한다면
        result_message = error_message
        # 아래의 에러 메세지를 표출 한다
    print(result_message)
    # 그 후 에러메세지 초기화
    result_message = ""






