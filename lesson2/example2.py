import time
from datetime import datetime
import asyncio

time_coeff = 0.2


async def dish(name, prepare, wait):
    print(f"start: {datetime.now().strftime('%HH:%MM:%SS')} prepare {name}, {prepare} min")
    await asyncio.sleep(time_coeff * prepare)
    print(f"start: {datetime.now().strftime('%HH:%MM:%SS')} wait {name}, {wait} min")
    await asyncio.sleep(time_coeff * wait)
    print(f"{datetime.now().strftime('%HH:%MM:%SS')} dish {name} is ready!")


async def main():
    tasks = [
        asyncio.create_task(dish("Закуска", 2, 3)),
        asyncio.create_task(dish("Основное блюдо", 5, 10)),
        asyncio.create_task(dish("Десерт", 3, 5))
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    t0 = time.time()
    asyncio.run(main())
    dt = (time.time() - t0) / time_coeff
    print(f"{datetime.now().strftime('%HH:%MM:%SS')} It took {dt} time")
