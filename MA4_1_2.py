
"""
Solutions to module 4
Review date:
"""

student = "Oliver Johansson"
reviewer = ""

import math as m
import random as r

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere
    f = lambda x: x**2
    lst=[[f(r.uniform(-1,1)) for i in range(d)] for i in range(n)]
    filtlist = list(filter(filt,lst))
    ratio = len(filtlist)/n
    kubvolym = 2**d
    volym = ratio * kubvolym

    return volym

def filt(num):
    if sum(num) <= 1:
        return True
    else:
        return False

def hypersphere_exact(n ,d):
    exact = (m.pi**(d/2))/m.gamma((d/2)+1)
    return exact
    
def main():
    dlist = [2,11]
    n = 100000
    for d in dlist:
        sphere = sphere_volume(n,d)
        hyper = hypersphere_exact(n,d)
        print(f"the volume of a sphere with {d} dimensions and {n} dots is {sphere}")
        print(f"riktiga volymen för en sphere med {d} dimensioner är:  {hyper}")


if __name__ == '__main__':
	main()
