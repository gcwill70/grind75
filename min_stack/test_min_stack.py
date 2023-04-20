from min_stack.min_stack import MinStack


def test1():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    stack.top() == 0
    assert stack.getMin() == -2


def test2():
    stack = MinStack()
    stack.push(5)
    stack.push(6)
    stack.push(3)
    stack.push(7)
    assert stack.getMin() == 3
    stack.pop()
    assert stack.getMin() == 3
    stack.pop()
    assert stack.getMin() == 5


def test3():
    stack = MinStack()
    stack.push(5)
    stack.push(6)
    stack.push(3)
    stack.push(7)
    assert stack.top() == 7
    stack.pop()
    assert stack.top() == 3
    stack.pop()
    assert stack.top() == 6
