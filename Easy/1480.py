nums = [1,2,3,4,5]
out = [nums[0]]

for i in range(1, len(nums)):
    out.append(out[i-1] + nums[i])

print(out)
