class Solution:#brute force solution
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(0, len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                ans = max(ans, current_sum)
        return ans

#Kadane's algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxi = float("-inf")
        for i in range(0,len(nums)):
            total = total+nums[i]
            maxi = max(total,maxi)
            if total < 0:
                total = 0

        return maxi
