import asyncio
import os
from random import randint

ITER_NUM = 10
COROUT_NUM = 5


async def do_some_work(i):
    for j in range(ITER_NUM):
        print(format_work(i, j))
        await asyncio.sleep(0.01 * randint(1, 10))


async def main():
    tasks = []
    for i in range(COROUT_NUM):
        tasks.append(asyncio.create_task(do_some_work(i)))
    await asyncio.gather(*tasks)


def format_work(i, j):
    return i * ' ' + "█" + (COROUT_NUM - i) * ' ' + f'cr {i} iter {j} ' + "■" * j


if __name__ == '__main__':
    asyncio.run(main())
