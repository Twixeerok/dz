class Tree:
    def __init__(self, name) -> None:
        self.heigth = 0
        self.age = 0 
        self.name = name

    def info(self):
        return f'{self.heigth}|{self.age}|{self.name}'

    def grow(self):
        self.age += 1
        self.heigth = 2 ** self.age
 


class FruiTree(Tree):
    def __init__(self, name, kol) -> None:
        self.kol = kol
        super().__init__(name)

    def get_fruits(self):
        self.kol = self.age / 2
        print(self.kol)

a = FruiTree('all', 2)
a.grow()
a.grow()
a.grow()
a.get_fruits()
print(a.info())