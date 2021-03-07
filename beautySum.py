from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        if len(s) < 3:
            return 0
        n = len(s)
        ref = list(range(2, n ))
        ans = 0
        see = []
        while ref:
            left = 0
            right = ref.pop(0)
            info = Counter(s[left:right+1])
            see.append(s[left:right+1])
            ans += max(info.values()) - min(info.values())
            while right < n - 1:
                out_data = s[left]
                right = right+1
                left += 1
                in_data = s[right]
                see.append(s[left:right+1])
                if in_data not in info:
                    info[in_data] = 1
                else:
                    info[in_data] += 1
                info[out_data] -= 1
                if info[out_data] <= 0:
                    del info[out_data]
                ans += max(info.values()) - min(info.values())
                # left += 1
                # right += 1
        print(see)
        return ans


if __name__ == "__main__":
    s = "bflcpbokxoiqhlmqciqrrztyzpprsqdpijfxgjlwrdebyupwctklydxckumfnzplrywdwdftopoekjtyepqvfnmbqzclyvsjckeufxebxschiaxfcqlnnxhvdpxecfwmjccdxlnzkeqhajkeqfpruxudduxfzkgbzxelgeqxiqyaptwzlbnyeudykdxpafmqtckhtvsarzquitoterprwsxkttnehvrmwwaedrtypnerbghjcofvxaixclkfbbnsidhpsturyxmtfmqhzhktytfjoubdazxkghyjyaugvivuovqpxprhxqvfqprmwnuityjmesmkskragmzrigoqrkvxxbnljlmknicjdjzynweurkdybhjxcvtctxmfbgapkythgayxpuhlkiplumcpidbrghfwgroycxrmuqwwvsjjjbbpmkcpbmfoxmnqxazarvbgjknaqfsnehsrugkktgogpfrwrnrnwpaednxexeqvjzorrgtp"
    print(Solution().beautySum(s))