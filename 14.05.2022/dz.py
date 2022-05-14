
from threading import Thread
import time
from multiprocessing import Process, Lock


class Th(Thread):
    def __init__(self, iteration, value):
        Thread.__init__(self)
        self.iteration = iteration
        self.value = value

    def run(self):
        a = [open(f'14.05.2022/2/iteration Thread{i}.txt', 'a').close() for i in range(self.iteration)]
        for i in range(self.iteration):
            print(f'iteration Thread{i}')
        
        

    def pr(self):
        s = [open(f'14.05.2022/2/iteration{i}.txt', 'a').close() for i in range(self.iteration)]
        for i in range(self.iteration):
            print(f'iteration{i}')

        
    def f(self):
        lock = Lock()
        lock.acquire()
        try:
            [open(f'14.05.2022/3/iteration Process{i}.txt', 'a').close() for i in range(self.iteration)]
            print(f'iteration Process {num}')
        finally:
            lock.release()







if __name__ == '__main__':
    t = Th(5, 1)
    t.start()
    t.pr()

    for num in range(5):
        Process(target=t.f()).start()