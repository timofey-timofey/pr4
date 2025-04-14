'''
Задание 1

import math

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + self.side1 + self.side2

circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

triangle = Triangle(4, 3, 5, 6)
print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())
'''
'''
Задание 2

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Двигатель автомобиля запущен.")

    def stop_engine(self):
        print("Двигатель автомобиля остановлен.")

class Bike(Vehicle):
    def start_engine(self):
        print("Двигатель мотоцикла запущен.")

    def stop_engine(self):
        print("Двигатель мотоцикла остановлен.")

car = Car()
car.start_engine()
car.stop_engine()

bike = Bike()
bike.start_engine()
bike.stop_engine()
'''
'''
Задание 3
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

sorted_people = sorted(people, key=lambda x: x['age'])

print("Сортированные по возрасту:")
for person in sorted_people:
    print(person)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 15, 23, 42, 5, 7, 13, 9, 6]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Простые числа:")
print(prime_numbers)
'''
'''
Задание 4
class BankAccount:
    def __init__(self):
        self.__balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Счет пополнен на {amount}. Текущий баланс: {self.__balance}.")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Ошибка: недостаточно средств на счете.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Снято {amount}. Текущий баланс: {self.__balance}.")
        else:
            print("Сумма снятия должна быть положительной.")

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
account.withdraw(30)
account.withdraw(100)
print(f"Баланс: {account.get_balance()}.")
'''
'''
Задание 5
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(4, 5)
print(f"Площадь прямоугольника: {rect.area()}.")  
print(f"Периметр прямоугольника: {rect.perimeter()}.") 
'''