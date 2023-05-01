from letter_combinations import Solution


def test1():
    assert set(Solution().letterCombinations("23")) == set(
        [
            "ad",
            "ae",
            "af",
            "bd",
            "be",
            "bf",
            "cd",
            "ce",
            "cf",
        ]
    )


def test2():
    assert set(Solution().letterCombinations("2")) == set(["a", "b", "c"])


def test3():
    assert set(Solution().letterCombinations("3")) == set(["d", "e", "f"])
