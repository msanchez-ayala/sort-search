import pytest
from data_structures.stack import Stack, SizeError
from data_structures.node import Node

@pytest.fixture
def stack():
    return Stack()

class TestStack:
    def test_init(self, stack):
        assert stack.top == None, 'Stack not empty'
        assert stack.capacity == 10, 'Default capacity not assigned'
        assert stack.size == 0

        node = Node(5)
        stack = Stack(node)
        assert stack.top.value == 5\
            , 'Node with value 5 not properly assigned to stack'
        assert stack.size == 1\
            , 'Stack size doesn\'t reflect that there is only 1 node.'
    
    def test_push(self, stack):
        stack.push(5)
        assert stack.top.value == 5, 'Node not properly pushed'
        assert stack.size == 1\
            , 'Stack size doesn\'t reflect that there is only 1 node.'

        stack.push(4)
        assert stack.top.value == 4, 'Node not properly pushed'
        assert stack.top.next.value == 5\
            , 'Reference to next node was not established correctly'
        assert stack.size == 2\
            , 'Stack size doesn\'t reflect that there are 2 nodes.'

    def test_push_error(self):
        stack = Stack(capacity = 0)
        with pytest.raises(SizeError):
            stack.push(5)

    def test_pop(self):
        stack = Stack(Node(5))
        assert stack.pop() == 5, 'Popped node was not the top node'
        assert stack.top == None\
            , 'There should be no top node'
        assert stack.size == 0\
            , 'Size should be 0 since 1 node was popped from 1 node stack'
    
    def test_pop_error(self, stack):
        with pytest.raises(SizeError):
            stack.pop()

    def test_peek(self, stack):
        assert stack.peek() == None\
            , 'There is no top node, but peek is returning a value'
        
        stack.push(5)
        assert stack.peek() == 5\
            , 'Top node has value 5 but this is not being returned'
    
    def test_is_empty(self, stack):
        assert stack.is_empty() == True\
            , 'Stack is empty but method returns False'
        
        stack.push(5)
        assert stack.is_empty() == False\
            , 'Stack is not empty but method returns True'
    
    def test_is_full(self):
        stack = Stack(capacity = 2)
        assert stack.is_full() == False\
            , 'Stack is empty with capacity of 2 but method returns True'
        
        stack.push(5)
        assert stack.is_full() == False\
            , 'Stack has nodes but not full yet method returns True'
        
        stack.push(4)
        assert stack.is_full() == True\
            , 'Stack is full but method does not reflect that'