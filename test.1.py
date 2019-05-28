from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random


def dice(n):
    test = []
    randcount = 0
    while randcount < n:
        test.append(random.randint(1,6))
        randcount = randcount + 1
    plt.hist(test, bins = [1,2,3,4,5,6])
    plt.savefig("new_piks.png")
