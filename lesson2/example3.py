import time
from random import randint

ITER_NUM = 10  # количество итераций в каждом воркере
COROUT_NUM = 5  # необходимое количество воркеров


def do_some_work(i):
    for j in range(ITER_NUM):
        print(format_work(i, j))
        time.sleep(0.01 * randint(1, 10))


def main():
    for i in range(COROUT_NUM):
        do_some_work(i)


def format_work(i, j):
    return i * ' ' + "█" + (COROUT_NUM - i) * ' ' + f'cr {i} iter {j} ' + "■" * j


if __name__ == '__main__':
    main()