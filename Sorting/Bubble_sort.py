class Solution:
    def bubbleSort(self,arr):
        # code here
        for i in range(len(arr)-2,-1,-1):
            for j in range(0,i+1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr

#for each run of the main for loop, the highest element bubbles up