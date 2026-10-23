# Python Basics to Advanced Example
# Run: python async_generator.py

import asyncio

async def numbers():
    for n in range(3):
        await asyncio.sleep(0)
        yield n

async def main():
    print([n async for n in numbers()])

asyncio.run(main())
