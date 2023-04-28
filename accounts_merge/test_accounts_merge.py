from accounts_merge import Solution


def test1():
    accounts = Solution().accountsMerge(
        [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
    )
    assert (
        accounts.index(
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"]
        )
        != -1
    )
    assert accounts.index(["Mary", "mary@mail.com"]) != -1
    assert accounts.index(["John", "johnnybravo@mail.com"]) != -1


def test2():
    accounts = Solution().accountsMerge(
        [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        ]
    )
    assert accounts.index(["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"]) != -1
    assert (
        accounts.index(
            ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
        )
        != -1
    )
    assert accounts.index(["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"]) != -1
    assert accounts.index(["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"]) != -1
    assert accounts.index(["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]) != -1


def test3():
    accounts = Solution().accountsMerge(
        [
            ["David", "David0@m.co", "David1@m.co"],
            ["David", "David3@m.co", "David4@m.co"],
            ["David", "David4@m.co", "David5@m.co"],
            ["David", "David2@m.co", "David3@m.co"],
            ["David", "David1@m.co", "David2@m.co"],
        ]
    )
    assert (
        accounts.index(
            [
                "David",
                "David0@m.co",
                "David1@m.co",
                "David2@m.co",
                "David3@m.co",
                "David4@m.co",
                "David5@m.co",
            ]
        )
        != -1
    )
