import pytest
from data_structures.queue import Queue
from data_structures.node import Node

class TestQueue:
    def test_init(self):
        queue = Queue()
        assert queue.rear == None, 'Rear wrongfully assigned a value'
        assert queue.front == None, 'Front wrongfully assigned a value'

        queue = Queue(Node(1))
        assert queue.rear.value == 1\
            , 'Rear node value not assigned correctly'
        assert queue.front.value == 1\
            , 'Front node value not assigned correctly'
        assert queue.front.next == None\
            , 'Front node has a reference to another when it should not.'
        
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        assert queue.rear.value == 1\
            , 'Rear node value not enqueued correctly'
        assert queue.front.value == 1\
            , 'Front node value not enqueued correctly'

        queue.enqueue(2)
        assert queue.rear.value == 2\
            , 'Rear node value not enqueued correctly'
        assert queue.front.value == 1\
            , 'Front node value was incorrectly affected'
        assert queue.front.next == queue.rear\
            , 'Proper relationship between nodes not established.'
    
    def test_dequeue(self):
        queue = Queue()
        front = Node(1)
        middle = Node(2)
        rear = Node(3)

        queue.front = front
        queue.front.next = middle
        middle.next = rear
        queue.rear = rear

        assert queue.dequeue() == 1\
            , 'Returned value is not the front node\'s value'
        assert queue.front == middle\
            , 'Front node was not removed or referencing is incorrect'
        assert queue.front.next == queue.rear\
            , 'Node referencing was incorrectly affected'

    def test_peek(self):
        queue = Queue()
        front = Node(1)
        rear = Node(2)

        queue.front = front
        queue.front.next = rear
        queue.rear = rear

        assert queue.peek() == 1\
            , 'Not returning the top node\'s value'
        assert queue.front == front\
            , 'Peek affected the node structure when it shouldn\'t have'
        assert queue.rear == rear\
            , 'Non-front nodes affected by peek'