# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:23:17 2022

@author: Jonas
"""

import asyncio

async def count_standard():
    print("Standard One")
    await asyncio.sleep(3)
    print("Standard Two")
    await asyncio.sleep(3)
    print("Standard Three")

async def count_fast():
    print("Fast One")
    await asyncio.sleep(1)
    print("Fast Two")
    await asyncio.sleep(1)
    print("Fast Three")


async def count_slow():
    print("Slow One")
    await asyncio.sleep(5)
    print("Slow Two")
    await asyncio.sleep(5)
    print("Slow Three")

async def test():
    await asyncio.gather(count_standard(), count_fast(), count_slow())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(test())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
