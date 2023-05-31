class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        max_pal = -1
        ans = None

        for i in range(l):
            c = s[i]

            for j in range(i+1, l):
                if s[j] == c:
                    pos_p = s[i:j+1]
                    len_p = len(pos_p)

                    if pos_p == pos_p[::-1] and len_p > max_pal:
                        max_pal = len_p
                        ans = pos_p
        
        if ans is None:
            ans = s[0]
                    
        return ans    


sol = Solution()
print(sol.longestPalindrome("ccc"))