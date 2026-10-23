# Python Basics to Advanced Example
# Run: python asyncio_demo.py

import asyncio

async def task(name):
    await asyncio.sleep(0.1)
    return f"{name} complete"

async def main():
    results = await asyncio.gather(task("A"), task("B"), task("C"))
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
