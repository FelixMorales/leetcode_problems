class Solution:
    def lengthOfLongestSubstring(self, s: str):
        current_set = set()
        highest_length = 0
        n = 0

        s_len = len(s)

        if s_len == 1:
            return 1
        
        for i in range(s_len):
            c = s[i]
            print(c)
            print(current_set)
            if c not in current_set:
                current_set.add(c)
                n += 1
            else:
                if n >= highest_length:
                    highest_length = n

                current_set = set(c)
                n = 1
                if i > 0:
                    current_set, new_n = self.checkLastString(i, s, c, current_set)
                    n += new_n
                print(current_set)

        if n >= highest_length:
            highest_length = n

        return highest_length
            
    def checkLastString(self, current_i, s, current_c, current_set: set):
        n = 0
        while current_i >= 0:
            current_i -= 1
            c = s[current_i]

            if c != current_c:
                current_set.add(c)
                n += 1
            else:
                break
        return current_set, n




sol = Solution()

print(sol.lengthOfLongestSubstring("anvinj"))
