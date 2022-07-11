from time import sleep
from random import randint


if __name__ == '__main__':
    while True:
        print('The random number is', randint(0, 1000))
        sleep(5)
