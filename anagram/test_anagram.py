from anagram.anagram import Solution


def test1():
    assert Solution().isAnagram("anagram", "nagaram")


def test2():
    assert not Solution().isAnagram("rat", "car")


def test3():
    assert Solution().isAnagram("", "")
