class Solution:#for duplicates
    def search(self, nums: list[int], target: int) -> bool:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]:#check for repeating sequence
                low += 1
                high -= 1
                continue#so that go back up to check if again same
            if nums[mid] <= nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
            else:
                if nums[low]<=target<=nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
        return False



        