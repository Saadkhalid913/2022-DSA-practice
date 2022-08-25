'''

LINK: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/

'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        RotIndex = self.FindRotIndex(nums)
        return nums[(RotIndex + 1) % (n)]

        
    
    def FindRotIndex(self, nums):
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


# Runtime: 44 ms, faster than 41.17% of Python online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 13.7 MB, less than 28.10% of Python online submissions for Find Minimum in Rotated Sorted Array.
        
        