# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:34:11 2022

@author: Jonas
"""



def count():
    print("One")
    time.sleep(1)
    print("Two")

def test():
    count()
    count()
    count()

if __name__ == "__main__":
    import time
    s = time.perf_counter()

    test()

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
