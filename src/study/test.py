'''
Created on 18Jul.,2017

@author: DINESHKB
'''

import math

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1
        print(number)
        

def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    next_prime = 1
    for next_prime in get_primes(next_prime + 2):
        if next_prime < 20:
            total += next_prime
            # print("next prime:", next_prime)
        else:
            print("total:", total)
            return


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


import random

def get_data():
    """Return 3 random integers between 0 and 9"""
    return random.sample(range(10), 3)

def consume():
    """Displays a running average across lists of integers sent to it"""
    running_sum = 0
    data_items_seen = 0

    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_items_seen)))

def produce(consumer):
    """Produces a set of values and forwards them to the pre-defined consumer
    function"""
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield

if __name__ == '__main__':
    csr = consume()
    csr.send(None)
    producer = produce(csr)

    for _ in range(10):
        print('Producing...')
        next(producer)