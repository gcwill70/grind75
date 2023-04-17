from queue_using_stacks.queue_using_stacks import MyQueue


def test1():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3


def test2():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.pop() == 1
    q.push(3)
    assert q.pop() == 2
    assert q.pop() == 3


def test3():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3
