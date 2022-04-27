# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:23:17 2022

@author: Jonas
"""

import asyncio

async def count():
    print("One")
    await asyncio.sleep(.5)
    print("Two")
    await asyncio.sleep(.5)
    print("Three")

async def test():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(test())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
