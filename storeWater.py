class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        if not bucket or not vat:
            return 0
        ans = 0
        ref_vat = []
        ref_bucket = []
        for idx, val in enumerate(zip(vat, bucket)):
            a, b = val
            if a == 0:
                continue
            if 0 == b:
                b += 1
                ans += 1
            ref_vat.append(a)
            ref_bucket.append(b)

        if not ref_vat:
            return ans
        tmp = [v // b + int(v % b != 0) for v, b in zip(ref_vat, ref_bucket)]
        res = float("inf")
        for ref in range(1, max(tmp) + 1):
            d = ans
            d += ref
            for i in range(len(tmp)):
                if ref_vat[i] // ref + int(ref_vat[i] % ref != 0) - ref_bucket[i] > 0:
                    d += ref_vat[i] // ref + int(ref_vat[i] % ref != 0) - ref_bucket[i]
            res = min(d, res)
        return res