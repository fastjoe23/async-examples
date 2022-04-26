# -*- coding: utf-8 -*-
"""
Created on Fri Apr  18 21:23:17 2022

@author: Jonas
"""
import timeit
import aiofiles
import asyncio

number_of_reads = 20

async def async_range(count):
    for i in range(count):
        yield(i)

async def read_file(file):
    #print("Read File: ", file)
    async with aiofiles.open(file, mode="r") as file:
        content = await file.read()
    file.close()

async def main():
    start_time = timeit.default_timer()

    # Asynchronous File Read
    async for i in async_range(number_of_reads):
        await asyncio.gather(read_file("test1.txt"), read_file("test2.txt"))
        #print(i)

    elapsed = timeit.default_timer() - start_time

    print("Elapsed Time: ", elapsed)

asyncio.run(main())
