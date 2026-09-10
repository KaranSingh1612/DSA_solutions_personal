class Solution:
    def insertionSort(self, arr):
        # code here
        for i in range(1, len(arr)):
            key = arr[i] #stores the current element as it may get lost
            j = i-1 #checks the sorted sub array before
            while j>=0 and arr[j]>key:
                arr[j+1] = arr[j]#shifts the larger element to right
                j -=1
                
            arr[j+1] = key#once the loop is exited, moves the key in place
            
        return arr