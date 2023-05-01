from palindromic_substrings import Solution


def test1():
    assert Solution().countSubstrings("abc") == 3


def test2():
    assert Solution().countSubstrings("aaa") == 6
