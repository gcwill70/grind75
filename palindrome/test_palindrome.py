from palindrome.palindrome import Solution


def test1():
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")


def test2():
    assert not Solution().isPalindrome("race a car")


def test3():
    assert not Solution().isPalindrome(" ")
