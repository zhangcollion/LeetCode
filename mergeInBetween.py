# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = 0
        head = list1
        if a == 1:
            next_head = list1
            left = list1
        else:
            while start < a-1:
                node = list1.next
                start += 1
                list1 = node
            next_head = node
            left = node
        while start <= b+1:
            right = left
            node = left.next
            start += 1
            left = node
        next_head.next = list2
        while list2:
            pre = list2
            list2 = list2.next
        pre.next = right
        return head


