# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        group, cur = 2, head
        while cur.next:
            cur = self.process_one_group(cur, group)
            group += 1
        return head

    def process_one_group(self, tail_of_last, n):
        cur, count = tail_of_last, 0
        while cur.next and count < n:
            cur = cur.next
            count += 1
        if count % 2 == 0:
            start, end = tail_of_last, tail_of_last.next
            for i in range(count - 1):
                # delete the node
                moved_node, end.next = end.next, end.next.next
                # insert the moved_node
                start.next, moved_node.next = moved_node, start.next
        cur = tail_of_last
        for i in range(count):
            cur = cur.next
        return cur
