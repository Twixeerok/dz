class Pet:
    def __init__(self,name) -> None:
        self.name = name

    def Names(self):
        return f'Имя питомца {self.name}'

class Cat(Pet):
    def __init__(self, name, say) -> None:
        super().__init__(name)
        self.say = say

    def may(self):
        print(f'Питомец {self.name}, сказал {self.say}')

class Dog(Pet):
    def __init__(self, name, say) -> None:
        super().__init__(name)
        self.say = say

    def gav(self):
        print(f'Питомец {self.name}, сказал {self.say}')


if __name__ == '__main__':
    a = Pet('barsik')
    print(a.Names())
    i = Cat('barsik', 'may')
    i.may()
    s = Dog('druzhok', 'gav')
    s.gav()