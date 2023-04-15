from linked_list_cycle.linked_list_cycle import Solution
from utils.listnode import ListNode


def test1():
    assert Solution().hasCycle(None) == False


def test2():
    root = ListNode.fromList([3, 2, 0, -4])
    root.next.next.next = root.next
    assert Solution().hasCycle(root) == True


def test3():
    assert Solution().hasCycle(ListNode.fromList([1, 2])) == False


def test4():
    assert Solution().hasCycle(ListNode.fromList([1])) == False
