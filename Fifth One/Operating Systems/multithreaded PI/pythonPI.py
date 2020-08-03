import multiprocessing
from multiprocessing import Queue, Pool
from decimal import Decimal, getcontext
import time
import random
import math

numberOfProcess = 2


def BBP(index):
    getcontext().prec = 10000
    temp = Decimal(0)
    for i in range(0, 1000):
        if i % numberOfProcess == index:
            temp += Decimal(Decimal(1)/16**i*(Decimal(4)/(8*i+1)-Decimal(2)/(8*i+4)-Decimal(1)/(8*i+5)-Decimal(1)/(8*i+6)))
    return temp


def SPIGOT(index):
    getcontext().prec = 10000
    temp = Decimal(0)
    for i in range(0, 1000):
        if i % numberOfProcess == index:
            temp += Decimal(math.factorial(i)**2) * 2**(i+1) / math.factorial(2*i+1)
    return temp


def NEWTON(index):
    getcontext().prec = 10000
    temp = Decimal(0)
    for i in range(0, 1000):
        if i % numberOfProcess == index:
            temp += Decimal(math.factorial(2*i)) / (2**(4*i+1))*(Decimal(math.factorial(i)**2)) * (2*i+1)
    return temp


def LEIBNIZ(index):
    getcontext().prec = 10000
    temp = Decimal(0)
    for i in range(0, 1000):
        if i % numberOfProcess == index:
            temp += Decimal(-3)**(-i)/(2*i + 1)
    return Decimal(math.sqrt(12)) * temp


def MONTECARLO(index):
    getcontext().prec = 10000
    temp = Decimal(0)
    for i in range(0, 1000000):
        if i % numberOfProcess == index:
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if x**2 + y**2 < 1 :
                temp += 1
    return 4 * temp/1000000


if __name__ == "__main__":


    startTime = time.time()
    
    lis = []

    with Pool(numberOfProcess) as p:
        lis = p.map(SPIGOT, ([i for i in range(numberOfProcess)]))

    finishTime = time.time()

    duration = finishTime - startTime


    print(f"executed in {duration} ms. with {numberOfProcess} processes running.")

    getcontext().prec = 10000

    res = Decimal(0)
    for i in lis:
        res += i
    
    print(f"Pi : {res}")