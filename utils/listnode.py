class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def fromList(l: list):
        if not l:
            return None
        head = ListNode(l[0])
        node = head
        for i in range(1, len(l)):
            node.next = ListNode(l[i])
            node = node.next
        return head
