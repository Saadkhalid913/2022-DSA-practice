'''

LINK: https://leetcode.com/problems/contains-duplicate/submissions/

'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # first method, takes advantage of speedy 
        # python builtins 
        l = list(set(nums))
        if len(l) != len(nums):
            return True 
        else:
            return False 
        
#  2nd method, uses hashmap  
#         seen = {}
#         for i, x in enumerate(nums):
#             if x in seen:
#                 return True 
#             else:
#                 seen[x] = True 
        
#         return False 
        

# Runtime: 647 ms, faster than 57.79% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 25.7 MB, less than 97.31% of Python3 online submissions for Contains Duplicate.
