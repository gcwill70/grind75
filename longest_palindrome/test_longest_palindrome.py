from longest_palindrome import Solution


def test1():
    assert Solution().longestPalindrome("babad") in ["aba", "bab"]


def test2():
    assert Solution().longestPalindrome("cbbd") in ["bb"]
