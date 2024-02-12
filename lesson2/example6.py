import os
from time import time
import asyncio
import aiohttp


async def get_file(i, url, session):
    print(f"getting file number {i}")
    response = await session.get(url, allow_redirects=True)
    await write_file(i, response)
    response.close()


async def write_file(i, response):
    print(f"writing file number {i}")
    filename = response.url.name
    data = await response.read()
    with open(f'./img/{filename}', 'wb') as file:
        file.write(data)


async def main():
    url = 'https://loremflickr.com/640/480'
    tasks = []
    session = aiohttp.ClientSession()
    for i in range(30):
        task = asyncio.create_task(get_file(i, url, session))
        tasks.append(task)
    await asyncio.gather(*tasks)
    await session.close()


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    print(f'{time() - t0} seconds')