

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        total_digits = 0
        module = 1
        stop = False
        
        while stop == False:
            module = module * 10
            a = x % module

            if a == x:
                stop = True

            total_digits += 1
        
        module = module // 10
        inverted_x = 0

        for i in range(total_digits):
            digit = self.get_digit(x, i)
            inverted_x += digit * module
            module =  module // 10

        return x == inverted_x

    def get_digit(self, n, index):
        return n // 10**index % 10

sol_obj = Solution()
result = sol_obj.isPalindrome(x=535)
print(result)