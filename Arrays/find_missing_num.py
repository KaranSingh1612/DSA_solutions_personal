class Solution:# brute force with time complexity of 0[n^2]
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i


class Solution:#better time complexity
    def missingNumber(self, nums: List[int]) -> int:
        freq = {}
        for i in range(0,len(nums)+1):
            freq[i]=0

        for num in nums:
            freq[num]+=1
        for k,v in freq.items():
            if v == 0:
                return k

class Solution:#most optimal solution
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        for i in nums:
            sum += i

        return int(n*(n+1)/2 - sum)
     