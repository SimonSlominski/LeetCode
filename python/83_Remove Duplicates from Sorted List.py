# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        last_unique = head
        current = head.next

        while current:
            if current.val != last_unique.val:
                last_unique.next = current
                last_unique = current
            current = current.next

        last_unique.next = None

        return head
