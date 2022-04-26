# -*- coding: utf-8 -*-
"""
Created on Fri Apr  18 21:23:17 2022

@author: Jonas
"""
import timeit

number_of_reads = 20

def read_file(file):
    #print("Read File: ", file)
    file = open(file,"r")

    textContent = file.read()

    file.close

start_time = timeit.default_timer()

# Synchronous File Read
for i in range(number_of_reads):
    read_file("test1.txt")
    read_file("test2.txt")
    #print(i)

elapsed = timeit.default_timer() - start_time

print("Elapsed Time: ", elapsed)
