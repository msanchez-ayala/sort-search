import pytest
from data_structures.queue import Queue
from data_structures.node import Node

class testQueue:
    def test_init(self):
        queue = Queue()
        assert queue.top == None, 'Top wrongfully assigned a value'
        assert queue.bottom == None, 'Bottom wrongfully assigned a value'

        queue = Queue(Node(1))
        assert queue.bottom.value == 1\
            , 'Bottom node value not assigned correctly'

    def test_enqueue(self):
        pass

    def test_dequeue(self):
        pass

    def test_peek(self):
        pass