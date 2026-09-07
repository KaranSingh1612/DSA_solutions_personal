class Solution: 
    def selectionSort(self, arr):
        # code here
        
        for i in range(0,len(arr)):
            min_idx = i #assume a minimum value
            for j in range(i+1,len(arr)): #runs a sub loop for each min value to compare with all other elements
                if arr[j] < arr[min_idx]:
                    min_idx = j
                    
            arr[i], arr[min_idx] = arr[min_idx],arr[i] #if value assumed is less then the next value, we swapp them
        return arr