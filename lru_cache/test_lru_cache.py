from lru_cache import LRUCache


def test1():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1


def test2():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test3():
    # ["LRUCache", "put", "put", "get", "put", "put", "get"]
    # [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
    # [null, null, null, 2, null, null, -1]
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    assert cache.get(2) == 2
    cache.put(1, 1)
    cache.put(4, 1)
    assert cache.get(2) == -1
