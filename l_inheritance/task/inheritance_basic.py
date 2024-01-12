# 인간(부모)
class Person:
    # 이름, 나이
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 걷기(walk)
    def walk(self):
        # '두 발로 걷습니다' 출력
        print('두 발로 걷습니다.')


# 원숭이(자식)
class Monkey(Person):
    # 이름, 나이, 동물원 이름
    def __init__(self, name: str, age: int, zoo: str):
        super().__init__(name, age)
        self.zoo = zoo

    # 걷기(walk)
    def walk(self):
        super().walk()
        # '두 발로 걷습니다', '네 발로 걷습니다' 출력
        print('네 발로 걷습니다.')


kingkong = Monkey('콩순이', 90, '에버랜드')
kingkong.walk()