""" The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x^2 + y^2 = r^2. """

import random

def estimpi():
    circle = 0
    iterations = 100000

    for _ in range(1, iterations):
        x = random.random()
        y = random.random()

        if (x ** 2 + y **2) <= 1:
            circle += 1

    pi = 4*(circle/iterations)

    return pi

if __name__ == '__main__':
    print(estimpi())