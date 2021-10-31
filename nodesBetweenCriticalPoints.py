# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ref_data = []
        pre_data = -1
        post_data = -1
        current_data = -1
        min_data = 100000000000
        i = 0
        while head:
            if pre_data == -1:
                pre_data = head.val
                head = head.next
                i += 1
                continue
            if current_data == -1:
                current_data = head.val
                head = head.next
                i += 1
                continue
            post_data = head.val
            if pre_data < current_data and current_data > post_data:
                pre_data = current_data
                current_data = post_data
                if len(ref_data) > 0:
                    min_data = min(min_data, i - ref_data[-1])
                ref_data.append(i)
                head = head.next
                i += 1
                continue
            if pre_data > current_data and current_data < post_data:
                pre_data = current_data
                current_data = post_data
                if len(ref_data) > 0:
                    min_data = min(min_data, i - ref_data[-1])
                ref_data.append(i)
                head = head.next
                i += 1
                continue
            else:
                pre_data = current_data
                current_data = post_data
                head = head.next
                i += 1
                continue
        # print(ref_data)
        if len(ref_data) < 2:
            return [-1, -1]
        ref_data.sort()
        ans = [min_data, ref_data[-1] - ref_data[0]]
        return ans

