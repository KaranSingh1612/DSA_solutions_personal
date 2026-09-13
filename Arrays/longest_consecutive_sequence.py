#brute force solution
count = 0
max_count = 0
for i in range(0,len(nums)):
            a = nums[i]
            count = 1
            while a+1 in nums:
                count += 1
                a += 1
            max_count = max(max_count, count)
        #return max_count

#better
nums.sort()
count = 0
last_smallest = float("-inf")
longest = 0
for i in nums:
            if i-1 == last_smallest :
                count += 1               
                last_smallest = i
            elif i == last_smallest:
                pass

            else:
                count = 1
                last_smallest = i
            longest = max(count,longest)

#return longest

#optimal
nums_set = set(nums)
count = 0
longest = 0
for i in nums_set:
            
            if i-1 in nums_set:
                pass
            elif i-1 not in nums_set:
                num = i
                count = 1
                while num + 1 in nums_set:
                    count+=1
                    num +=1
                longest = max(longest,count)

        #return longest


        
        
        
            


        