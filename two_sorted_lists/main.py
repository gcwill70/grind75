from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 == None or list1 == []:
            return list2
        if list2 == None or list2 == []:
            return list1
        # Both lists are not empty
        first = list1
        second = list2
        cur = head = None
        # Merge list2 into list1
        while first != None and second != None:
            # Append First
            if first.val <= second.val:
                if cur == None:
                    cur = first
                else:
                    cur.next = first
                first = first.next
            # Append Second
            else:
                # insert second in front of first
                second = second.next
            # assign head
            head = cur if head == None else head
        # Append remaining list

        return head

    def append(self, node: ListNode, toAdd: ListNode):
        node.next
