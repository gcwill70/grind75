from courses.courses import Solution


def test1():
    assert Solution().canFinish(2, [[1, 0]]) == True


def test2():
    assert Solution().canFinish(2, [[1, 0], [0, 1]]) == False


def test3():
    assert Solution().canFinish(3, [[1, 0], [1, 2], [0, 1]]) == False


def test4():
    assert Solution().canFinish(3, [[1, 0], [1, 2]]) == True
