class Solution:
    def lengthOfLongestSubstring(self, s: str):
        n = len(s)
        max_len = 0
        d = {}

        i = 0
        for j in range(n):
            c = s[j]
            if c in d and d[c] >= i:
                i = d[c]

            subs_len = j - i + 1
            
            if subs_len >= max_len:
                max_len = subs_len

            d[c] = j + 1


        return max_len




sol = Solution()

print(sol.lengthOfLongestSubstring("azbzabt"))

"anviaj"
