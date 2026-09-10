class Solution:#Brute force solution -- O[n] time complexity and space complexity
    def moveZeroes(self, nums: List[int]) -> None:
        temp = []
        for i in range(0,len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])

        for j in range(0,len(temp)):
            nums[j] = temp[j]

        for k in range(len(temp),len(nums)):
            nums[k] = 0

