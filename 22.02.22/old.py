from doctest import master


class Dog:
    def __init__(self, height, weigth, name, age) -> None:
        self.height = height
        self.weigth = weigth
        self.name = name
        self.age = age

    def jump(self):
        print(f'{self.name} прыгает')
    
    def run(self):
        print(f'{self.name} бегает')
   
    def brack(self):
        print(f'{self.name} делает гав')

    def che(self):
        print(f'собака {self.name} имеет рост {self.height} вес {self.weigth} и возраст {self.age}')

    def change_name(self):
        self.name = 'barsik'
        print(self.name)

    def get_master(self, master):
        self.__master = master
        return self.__master

    def get_minsk(self):
        return self.__minsk

    def set_minsk(self, minsk):
        self.__minsk = minsk




class Pet:
    def __init__(self, name, age, master, height , weigth) -> None:
        self.name = name
        self.age = age
        self.master = master
        self.height = height
        self.weigth = weigth

    def run(self):
        print(f'{self.name} бегает')

    def jump(self):
        print(f'{self.name} прыгает')

    def birthday(self):
        self.age += 1
        print(f'{self.name} исполнилось {self.age}')
    
    def sleep(self):
        print(f'{self.name} спит')
     
    def change_weight(self, new_age):
        try:
            self.weigth += new_age
            print(f'Теперь вес питомца {self.weigth}')
        except:
            self.weigth += 0.2
            print(f'Теперь вес питомца {self.weigth}')
    
    def change_height(self, new_age):
        try:
            self.weigth += new_age
            print(f'Теперь рост питомца {self.height}')
        except:
            self.weigth += 0.2
            print(f'Теперь рост питомца {self.height}')


class Parrots(Pet):
    def fly(self):
        if self.weigth > 0.1:
            print(f'{self.name} летает')
        else:
            print('вес слишом большой')

class Cats(Pet):
    def may(self):
        print(f'{self.name} мяу')

class Dogs(Pet):
    def gav(self):
        print(f'{self.name} гав')

if __name__ == '__main__':
    a = Dog(30, 15, 'bro', 8, 21)
    a.jump()
    a.run()
    a.brack()
    a.che()
    a.change_name()
    print(a.get_master('andrey'))
    a.set_minsk('minsk')
    print(a.get_minsk())
    p = Pet('maykala', 11, 'maxim', 50, 11)
    p.change_weight(None)