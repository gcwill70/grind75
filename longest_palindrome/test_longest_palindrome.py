from longest_palindrome import Solution


def test1():
    assert Solution().longestPalindrome("babad") == "bab"


def test2():
    assert Solution().longestPalindrome("cbbd") == "bb"
