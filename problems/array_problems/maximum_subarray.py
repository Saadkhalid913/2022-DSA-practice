from __future__ import annotations
from typing import Any, List, Dict, Set, Type, NoReturn, Union

'''
LINK: https://leetcode.com/problems/maximum-subarray/submissions/

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        maxSubarrayValue = nums[0]
        currentSubarrayVal = 0
        for i, x in enumerate(nums):
            currentSubarrayVal = max(0, currentSubarrayVal)
            currentSubarrayVal += x 
            maxSubarrayValue = max(currentSubarrayVal, maxSubarrayValue)
        return maxSubarrayValue 
            
            
            
                
        
            
                
                
        
            
            
        


