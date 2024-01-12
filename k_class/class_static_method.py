class Student:
    status = '쉬는 중'

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    @staticmethod
    def print_start_time_of_study(): # self를 지워야함
        print("9시 땡")
        Student.status = '공부 중'


kwon = Student(10, 10, 10)
kwon = Student(20, 20, 20)
print(Student.status)


Student.print_start_time_of_study()
print(Student.status)