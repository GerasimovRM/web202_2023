# задание1, защита1, отдых, задание2, защита2
import asyncio
import time

TIME_COEFF = 0.01


async def do_task(name, *args):
    times_task1 = [args[0], args[1]]
    times_task2 = [args[2], args[3]]
    for n, (t1, t2) in enumerate([times_task1, times_task2], 1):
        print(f"{name} started the {n} task.")
        await asyncio.sleep(TIME_COEFF * t1)
        print(f"{name} moved on to the defense of the {n} task.")
        await asyncio.sleep(TIME_COEFF * t2)
        print(f"{name} completed the {n} task.")


async def interviews(*data):
    tasks = []
    for participant in data:
        tasks.append(do_task(*participant))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    asyncio.run(interviews(*data))
    print(time.time() - t0)