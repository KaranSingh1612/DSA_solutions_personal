p = 0
n = 1
new_nums = [0]*len(nums)
for i in range(0,len(nums)):
    if nums[i] > 0:
                new_nums[p] = nums[i]
                p += 2

    else:
                new_nums[n] = nums[i]
                n += 2

    #return new_nums
            