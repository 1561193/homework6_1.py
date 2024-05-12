# Создайте родительский (базовый) класс Car, который имеет свойство price = 1000000 и функцию 
# def horse_powers, которая возвращает количество лошадиных сил для автомобиля
# Создайте наследника класса Car - класс Nissan и преопределите свойство price, а так же переопределите
# функцию horse_powers
# Дополнительно создайте класс Kia, который так же будет наследником класса Car и переопределите так же
# свойство prica, а так же переопределите функцию horse_powers  

class Car:
    price = 1000000

    def __init__(self, price):
        self.price = price

    def __str__(self):
        return '{} price {}'.format(self.__class__.__name__, self.price)

    def horse_powers(self):
        print('horse_powers 60')


class Nissan(Car):

    def horse_powers(self): # метод переопределяет предназначение
        print('horse_powers 100')


class Kia(Car):

    def horse_powers(self):
        print('horse_powers 92')


nissan = Nissan(price='800000')
print(nissan)
nissan.horse_powers()


kia = Kia(price='750000')
print(kia)
kia.horse_powers()




        
    