
def my_decorator(func):
    def wrapper(arg):
        new_arg = [a for a in arg if a % 2]
        return func(new_arg)
    return wrapper

@my_decorator
def real_func(x):
    print(x)



my_list = [1, 2, 3, 4, 5, 6, 7, 8]


def my_decorator2(func):
    def wrapper(*args):
        return func(my_list[::-1])
    return wrapper

@my_decorator2
def my_func(numbers: list):
    print(numbers)



class dz:
    def __init__(self):
        self.x = [i for i in range(10, 15)]

        
    def num1(self):
        for i in self.x:
            print(f'порядковый номер строки {self.x.index(i)}, символ {i} ')


    s = (lambda **kwargs: {b*2: i for b, i in kwargs.items()})
    print(s(abc=42, de=21, daf=45))



if __name__ == "__main__":
    a = dz()
    a.num1()
    real_func([1, 2, 3, 4, 5, 6, 7, 8, ])
    my_func(my_list)
    

 
