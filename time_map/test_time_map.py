from time_map.time_map import TimeMap


def test1():
    map = TimeMap()
    map.set("foo", "bar", 1)
    assert map.get("foo", 1) == "bar"
    assert map.get("foo", 3) == "bar"
    map.set("foo", "bar2", 4)
    assert map.get("foo", 4) == "bar2"
    assert map.get("foo", 5) == "bar2"
