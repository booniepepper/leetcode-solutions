# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, source: ListNode) -> ListNode:
        reversed = None
        while source is not None:
            reversed = ListNode(source.val, next=reversed)
            source = source.next
        return reversed
