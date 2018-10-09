# -*- coding: utf-8 -*-
import re

import numpy

# TODO: Extend queue class?


class ProductQueue(object):

    class ProductQueueNode(object):
        def __init__(self, n: int):
            self.n = n
            self.next = None

    # TODO: strictly type everything
    # TODO: Add docstrings
    def __init__(self):
        self.head = None
        self.tail = None
        self._curr_product = 1
        self._length = 0
        self._num_zeros = 0

    def __len__(self):
        return self._length

    def add_node(self, n: int):
        new_node = self.ProductQueueNode(n=n)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
        if n == 0:
            self._num_zeros += 1
        else:
            self._curr_product *= n

    def get_product(self):
        if self._num_zeros:
            return 0
        else:
            return int(self._curr_product)

    def print_queue(self):
        print('→'.join(str(n) for n in self._print_queue_helper()))

    def _print_queue_helper(self):
        temp_node = self.head
        while temp_node:
            yield temp_node.n
            temp_node = temp_node.next

    def remove_node(self):
        if not self.head:
            raise ValueError('Queue empty')
        popped_node = self.head
        if popped_node.n == 0:
            self._num_zeros -= 1
        else:
            self._curr_product /= popped_node.n
        self._length -= 1
        if len(self) == 0:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
        return popped_node.n


def parse_grid(*, str grid):
    return numpy.array(
        [
            [int(x) for x in row.strip().split(' ')]
            for row in grid.split('\n')
            if row.strip()
        ],
    )


def remove_whitespace(*, str number_str):
    return re.sub(r'\s+', '', number_str)
