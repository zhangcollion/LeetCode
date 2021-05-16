class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums1_info = Counter(nums1)
        self.nums2_info = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2_info[self.nums2[index]] -= 1
        self.nums2[index] += val 
        self.nums2_info[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        
        ans = 0
        for i in self.nums1_info.keys():
            ans += self.nums1_info[i] * self.nums2_info[tot-i]
        return ans