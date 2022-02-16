class File:
    def __init__(self) -> None:
        self.file1 = open('text.txt', 'r')
        self.file2 = open('text.txt2', 'r')
        self.file3 = open('text.txt3', 'r')

    def read(self):
        a = self.file1.readlines()
        b = self.file2.readlines()
        print(f'{a} \n{b}')



class One(File):
    def dz(self):
        count = 0
        s = False
        for i, a in zip(self.file1, self.file2):
            count += 1
            if i != a:
                s = True
                break
        if s == True:
            print(f"Отличается строка {count}")
        else:
            print("Отличий нет")         



class Three(File):
    def re(self):
        lines = self.file1.read()
        a = []
        for i in lines:
            a.append(i)
        print(f'{a[0]}, {a[4]} {a[0:4]} {lines}')
        
    
class Two:
    def joj(self):
        with open('text.txt3', 'w') as flow:
            g = flow.writelines([input('text') for i in range(5)])

class Fore:
    def joj(self):
        with open('text.txt3', 'a') as flow:
            g = flow.writelines([input('text') for i in range(3)])



class main:
    def mai():
        a = int(input('от 1 до 4'))
        if a == 1:
            s = One()
            s.dz()
        elif a == 2:
            s = Two()
            s.joj()
        elif a == 3:
            s = Three()
            s.re()
        elif a == 4:
            s = Fore()
            s.joj()
        else:
            ('er')


if __name__ == '__main__':
    a = main
    a.mai()

