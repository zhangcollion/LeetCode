class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)

        len_data = min(word1_len, word2_len)

        ans = ""
        for i in range(len_data):
            ans += word1[i]
            ans += word2[i]

        if word1_len > word2_len:
            ans += word1[len_data:-1]
        if word1_len <word2_len:
            ans += word2[len_data:-1]


        return ans



