# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        curr = start = head

        for _ in range(k - 1): curr = curr.next
        node1 = curr

        while curr.next:
            curr = curr.next
            head = head.next

        node2 = head
        node1.val, node2.val = node2.val, node1.val

        return start
