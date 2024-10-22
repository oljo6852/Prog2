
"""
Solutions to module 4
Review date:
"""

student = "Oliver Johansson"
reviewer = ""

import math as math
import random as r
import matplotlib.pyplot as plt 

def approximate_pi(n):
    nc = 0
    x_in = []
    y_in = []
    x_ut = []
    y_ut = []

    for _ in range(n):
        x= r.uniform(-1,1)
        y= r.uniform(-1,1)
        check = x**2 + y**2
        if check <= 1:
            nc+=1
            x_in.append(x)
            y_in.append(y)
        else:
            x_ut.append(x)
            y_ut.append(y)
    pi = 4 * (nc/n)
    plt.figure(figsize=(8,8))
    plt.scatter(x_in,y_in, color = "red", label = "inside cirkel", s=1)
    plt.scatter(x_ut, y_ut, color='blue', label='Outside Circle', s=1)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title(f"Monte Carlo with {n} points, π ≈ {pi}")
    plt.legend(loc='upper right')
    
    plt.savefig('monte_carlo_pi.png')
    plt.show()
    return pi
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        aproximate = approximate_pi(n)
        print(f"Aproximation using {n} gives {aproximate}")
    print(math.pi)
if __name__ == '__main__':
	main()
