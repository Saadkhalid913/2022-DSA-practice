from __future__ import annotations
from typing import Any, List, Dict, Set, Type, NoReturn, Union

'''

LINK: https://leetcode.com/problems/3sum/

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
            