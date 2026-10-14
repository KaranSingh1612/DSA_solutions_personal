class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lowerbound(nums,target):
            lb  = -1
            low = 0
            high = len(nums)-1
            while low<=high:
                mid = (low+high)//2
                if nums[mid]>=target:
                    lb = mid
                    high = mid -1
                else:
                    low = mid +1

            return lb
        def upperbound(nums,target):
            ub  = -1
            low = 0
            high = len(nums)-1
            while low<=high:
                mid = (low+high)//2
                if nums[mid]>target:
                    ub = mid
                    high = mid -1
                else:
                    low = mid +1
                    
            return ub

        lb = lowerbound(nums, target)
        if lb == -1 or nums[lb] != target:
            return [-1, -1]
        ub = upperbound(nums, target)
        if ub == -1:
            ub = len(nums)
        return [lb, ub - 1]
        

        

        