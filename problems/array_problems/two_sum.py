from __future__ import annotations
from typing import Any, List, Dict, Set, Type, NoReturn, Union

'''

LINK: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We're going to save a hashmap for each element of the array, i
        # such that hash[i] = index_of_i.
        # then we will also check if target - i exists
        # in the hash, and we will return 
        # the index of current element (i) , and hash[target - i]
    
        seen = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [i, seen[target - num]]
            seen[num] = i
        
        
# Runtime: 63 ms, faster than 95.29% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 50.22% of Python3 online submissions for Two Sum.
