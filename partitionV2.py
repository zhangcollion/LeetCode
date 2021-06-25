# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        
        right = []
        left = []
        while head:
            if head.val < x:
                left.append(head.val)
            else:
                right.append(head.val)
            head = head.next
        flag = 1
        if left:
            flag = 0
            right_node = ListNode(left[0])
            head_noe = right_node
            for i in left[1:]:
                right_node.next =  ListNode(i)
                right_node = right_node.next
            
        if right:
            if flag == 0: 
                right_node.next = ListNode(right[0])
                right_node = right_node.next
            else:
                right_node = ListNode(right[0])
                head_noe = right_node
            for i in right[1:]:
                right_node.next =  ListNode(i)
                right_node = right_node.next
        return head_noe