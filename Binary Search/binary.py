#Iterative solution
def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1       
        while high>low:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return -1

#Recursive solution
def binarySearch(arr,low,high):
            if low>high :
                return -1
            mid = (low + high)//2
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                return binarySearch(arr, mid + 1, high)
            else:
                return binarySearch(arr,low, mid - 1)
            

#       return binarySearch(nums,0,len(nums)-1)