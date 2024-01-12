class Car:

    # 정적 변수(static variable)
    # 정적 변수는 컴파일러가 가장 먼저 메모리에 올라간다
    wheel = 4

    def __init__(self, brand='', color='', price=0):
        self.brand = brand
        self.color = color
        self.price = price

    def engine_start(self):
        print(self.brand + '시동 켜짐')

    def engine_end(self):
        print(self.brand + '시동 꺼짐')

# mom_car = Car(brand = 'kia', color = 'black', price = 100000000)
# daddy_car = Car(brand = 'hyundai', color = 'white', price = 150000000)
#
# mom_car.engine_start()
# daddy_car.engine_end()
#
# print(Car.wheel)
#
# Car. wheel = 6

# print(mom_car.wheel)

cars = [Car, Car,Car]
cars[0]()
mom_car = cars[0]()
daddy_car = cars[1]()
my_car = cars[2]()
print(mom_car, daddy_car, my_car, sep='\n')