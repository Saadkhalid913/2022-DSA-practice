from __future__ import annotations
from typing import Any, List, Dict, Set, Type, NoReturn, Union


'''
Link: https://leetcode.com/problems/product-of-array-except-self/submissions/

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = []
        postfix = []
        for i, x in enumerate(nums):
            if i == 0:
                prefix.append(x)
            else:
                prefix.append(x * prefix[i - 1])
        
        for i, x in enumerate(reversed(nums)):
            if i == 0:
                postfix.append(x)
            else:
                postfix.append(x * postfix[i - 1])
         # [1, 2, 3,  4] 2       
         # [1, 2, 6, 24] 1  
         # [4, 12,24, 24] 0
                
        answer = []
        for i, x in enumerate(nums):
            backproductIndex = i - 1
            backproduct = 1 
            if backproductIndex >= 0:
                backproduct = prefix[backproductIndex]
            
            frontproductIndex = n - i - 2
            frontproduct = 1
            if frontproductIndex >= 0:
                frontproduct = postfix[frontproductIndex]
            
            answer.append(backproduct * frontproduct)
        
        return answer 

# Runtime: 477 ms, faster than 13.75% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 22.4 MB, less than 18.46% of Python3 online submissions for Product of Array Except Self.
