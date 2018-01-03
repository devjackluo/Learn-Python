from multiprocessing import Process
import threading
import os
import time

one = 1
two = 2
three = 3

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    time.sleep(2)

def f(name):
    info('function f')
    print('hello', name)

def floop(name, x):
	
    for x in range(x):
    	info('function floop')
    	print('hello', name,  x,)


def addOne():

    for x in range(500):
        # one += 1
        # three += 1
        print(x)

def addTwo():

    for x in range(1000):
        # two += 2
        # three += 2
        print(x)




if __name__ == '__main__':

    info('main line')
    p = Process(target=f, args=('bob',))
    fl = Process(target=addOne, args=())
    fl2 = Process(target=addTwo, args=())
    #fl3 = Process(target=floop, args=())
    fl.start()
    fl2.start()
    #fl3.start()
    p.start()
    fl.join()
    fl2.join()
    #fl3.join()
    p.join()