# Brute force technology
class Solution:# time complexity O[n^3]
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        trip = [nums[i],nums[j],nums[k]]
                        trip.sort()
                        if trip not in result:
                            result.append(trip)

        return result

#better solution
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        nums.sort()
        
        for i in range(0, n):
            # Correct duplicate check for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    # Corrected pointer condition (j < k) for skipping duplicate values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                        
        return result
                