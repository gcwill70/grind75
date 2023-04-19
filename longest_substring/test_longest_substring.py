from longest_substring.longest_substring import Solution


def test1():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3


def test2():
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1


def test3():
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3


def test4():
    assert Solution().lengthOfLongestSubstring("") == 0


def test5():
    assert Solution().lengthOfLongestSubstring("a") == 1


def test6():
    assert Solution().lengthOfLongestSubstring("dvdf") == 3
