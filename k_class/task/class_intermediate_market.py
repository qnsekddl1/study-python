# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수
# class Product():
#     def __init__(self, product_name, product_price):
#         self.product_name = product_name
#         self.product_price = product_price
#         apple = Product(product_name='Apple', product_price=2000)
#         banana = Product(product_name='Banana', product_price=3000)
#
#     def print_product_info(product_name, product_price):
#         result = {'product_name': product_name, 'product_price': product_price}
#         return result
#
#         print(result)

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.
# class Market:
#     def __init__(self, product, stuck):
#         self.product = product
#
#     def sell(self, customer):
#         self.product.price - customer.discount



# 손님
# 이름, 나이, 할인율, 잔액
# class Customer:
#     def __init__(self, name, age, discount, balnce):
#         self.name = name
#         self.age = age
#         self.discount = float(discount)
#         self.balnce = float(balnce)
#
# 홍길동 = Oder(name= '홍길동', age= 20 ,discount=50, balance=)


# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.

# 손님
# 이름, 나이, 할인율, 잔액


class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print(self.name, self.price)

class Market:
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock


    def sell(self, customer):
        customer .money -= self.product.price * (1 - customer.discount * 0.01)
        self.stock -= 1

class Customer:
    def __init__(self, name, age, discount, money):
        self.name = name
        self.age = age
        self.discount = discount
        self.money = money

홍길동 = Customer(name= '홍길동', age= 20 ,discount=50, money=0)

product = Product('사과', 5000)
customer = Customer(name='이기영', age=20, discount=50, money=10000)
market = Market(product, 40)
market.sell(customer)
print(market.stock)
print(customer.money)









