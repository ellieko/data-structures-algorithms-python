# Data structure tutorial exercise: Queue
from collections import deque
import threading
import time


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    # exercise prob 1) food ordering system

    def place_order(self, orders):
        for order in orders:
            self.enqueue(order)
            time.sleep(0.5)

    def serve_order(self):
        while not self.is_empty:
            time.sleep(2)
            print(self.dequeue())

    def food_ordering_system(self, orders):
        q = Queue()
        t1 = threading.Thread(target=q.place_order, args=(orders,))
        t2 = threading.Thread(target=q.serve_order)
        t1.start()
        time.sleep(1)
        t2.start()
        t1.join()
        t2.join()


# exercise prob 2) print binary numbers from 1 to 10
def binary_numbers(n):
    q = Queue()
    q.enqueue('1')
    for i in range(n):
        entry = q.dequeue()
        print(entry)
        q.enqueue(entry + '0')
        q.enqueue(entry + '1')


if __name__ == '__main__':
    # exercise prob 1)
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    q = Queue()
    q.food_ordering_system(orders)  # not sure how to test

    # exercise prob 2)
    binary_numbers(10)
