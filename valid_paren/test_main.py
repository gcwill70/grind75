from main import Solution


def test_first():
    assert Solution().isValid("()")


def test_second():
    assert Solution().isValid("()[]{}")


def test_third():
    assert not Solution().isValid("(]")


def test_fourth():
    assert not Solution().isValid("([)]")
