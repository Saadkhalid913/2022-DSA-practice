



def FindRotIndex(nums):
        n = len(nums)
        if n == 1:
            return 0 
        
        startIdx, sortedIdx, endIdx = 0, n // 2, n

        while sortedIdx != endIdx:
            if nums[sortedIdx] > nums[startIdx]:
                startIdx = sortedIdx
                sortedIdx = (sortedIdx + endIdx) // 2
            else:
                endIdx = sortedIdx
                sortedIdx = (startIdx + sortedIdx) // 2

        return endIdx

a = [10,11,12,6,7,8,9] # 2
b = [1,2,3,4,-2,-1,0] # 3
c = [1] # 0
c = [1,2,3,4,5,6,7,8,9,10] # 0
d = [i for i in range(10, 50)] + [i for i in range(-10 ,10)] # 49 


print(FindRotIndex(c))
print(d[FindRotIndex(d)])


