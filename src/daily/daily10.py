""" Implement a job scheduler which takes in a function f and an integer n, and 
calls f after n milliseconds. """

from threading import Timer

def schedule(f, n):
    t = Timer(n/1000, f)
    t.start()

def hello():
    print("hello")

if __name__ == '__main__':
    schedule(hello, 1000)