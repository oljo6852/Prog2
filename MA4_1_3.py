"""
Solutions to module 4
Review date:
"""

student = "Oliver Johansson"
reviewer = ""

import math as m
import random as r
import concurrent.futures
from time import perf_counter as pc

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    f = lambda x: x**2
    lst = [[f(r.uniform(-1, 1)) for _ in range(d)] for _ in range(n)]
    filtlist = list(filter(filt, lst))
    ratio = len(filtlist) / n
    kubvolym = 2**d
    volym = ratio * kubvolym

    return volym 

def filt(num):
    return sum(num) <= 1

def hypersphere_exact(n, d):
    exact = (m.pi**(d / 2)) / m.gamma((d / 2) + 1)
    return exact


def sphere_volume_parallel1(n, d, np):
    with concurrent.futures.ProcessPoolExecutor(max_workers=np) as executor:
        results = list(executor.map(sphere_volume, [n]*np, [d]*np))
    return sum(results) / len(results)


def sphere_volume_parallel2(n, d, np):
    chunk_size = n // np
    chunks = [chunk_size] * np

    if n%np != 0:
        chunks[-1] += n % np

    with concurrent.futures.ProcessPoolExecutor(max_workers=np) as executor:
        results = list(executor.map(sphere_volume, chunks, [d]*np))
    return sum(results) / len(results)

def main():
    n = 100000
    d = 11
    np = 8 

    # Part 1: Sequential execution
    start_tid = pc()
    for _ in range(10):
        vol = sphere_volume(n, d)
        print(f"Volume is: {vol}")
        
    seq = pc() - start_tid
    print(f"Time: {seq:.2f} seconds and volume = {vol}")

    # PaRt 1: Parallel execution
    start_tid = pc()
    vol_par1 = sphere_volume_parallel1(n, d, np)
    par1 = pc() - start_tid
    print(f"Time: {par1:.2f} seconds gives volume = {vol_par1}")

    # Part 2: Sequential execution
    start_tid = pc()
    vol_seq = sphere_volume(n, d)
    seq2_elapsed = pc() - start_tid
    print(f"Time: {seq2_elapsed:.2f} seconds gives volume = {vol_seq}")

    # Part 2: Parallel execution
    start_tid = pc()
    vol_par2 = sphere_volume_parallel2(n, d, np)
    par2_elapsed = pc() - start_tid
    print(f"Time: {par2_elapsed:.2f} seconds gives volume= {vol_par2}")

if __name__ == '__main__':
    main()
