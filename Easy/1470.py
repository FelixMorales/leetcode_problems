nums = [2,5,1,3,4,7]
n = len(nums) // 2
out = [0]*(n*2)
j = 0
for i in range(n):
    out[j] = nums[i]
    out[j+1] = nums[i+n]
    j+= 2

print(out)