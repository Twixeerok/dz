from abc import ABC, abstractclassmethod
import random
class Human:
    def __init__(self, name) -> None:
        Human.name = name

    @classmethod
    def get_counter(cls):
        return cls.name

hu = Human('1')
hu1 = Human('2')
hu2 = Human('3')

print(Human.get_counter())


class Petsq:
    def __init__(self, name) -> None:
        self.name = name

    @staticmethod
    def get_random_name():
        pass




class Pets(ABC):
    @abstractclassmethod
    def voise(self):
        print('hello')

class Horse(Pets):
    def voise(self):
        print('ko-ko')

class Donkey(Pets):
    def voise(self):
        print('me-me')

class Mule(Donkey):
    pass


class Animal:
    def name(self):
        print('animal')


class Pet(Animal):
    def name(self):
        print('Pet')

class Cat(Pet):
    def name(self):
        print('Cat')

class Dog(Pet):
    def name(self):
        print('Dog')

class WildAnimal(Pet):
    def name(self):
        print('WildAnimal')

class Lion(WildAnimal):
    def name(self):
        print('Lion')

class Wolf(WildAnimal):
    def name(self):
        print('Wolf')



class Book:
    def __init__(self, num, years, author, price) -> None:
        self.num = num 
        self.years = years 
        self.author = author 
        self.price = price

    def lp(self):
        try:
            a = input('введите, что хотите узнать: кол-во страниц(страницы), год издания(год), автора(автор), цену(цена)')
            if a == 'страницы':
                print(self.num)
            elif a == 'год':
                print(self.years)
            elif a == 'автор':
                print(self.author) 
            elif a == 'цена':
                print(self.price)        
        except AttributeError as err:
            print(err)
        except NameError as err:
            print(err)
        except OSError as err:
            print(err)
        except SyntaxError as err:
            print(err)
        except TypeError as err:
            print(err)


class Matrix:
    def __init__(self) -> None:
        self.data = [[random.randrange(0, 10) for a in range(5)] for b in range(5)]

    def print(self):
        matrix = self.data
        self.q = []
        for i in range(len(matrix)):
            print(matrix[i])
            self.q.append(matrix[i])
    
    def sum(self):
        i = sum(self.q[0] + self.q[1])
        print(f'Сумма чисел равна: {i}')

    def minandmax(self):
        for i in self.q:
            a = min(i)
            q = max(i)
        print(f'минимальное число в матрице {a}, а максимальное {q}')



a = Matrix()
print(a)