from __future__ import annotations
from typing import Any, List, Dict, Set, Type, NoReturn, Union


'''

LINK: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # this is essentially a maximum difference problem, perhaps
        # similar to twosum. We need to keep track of the lowest value that
        # we have come accross and while we do not come accross a lower value, 
        # we keep track of the highest value 
        
        low = 10**5 + 1
        PLow = 10 ** 5 + 1
        high = 0
        for i,x in enumerate(prices):
            if x < PLow:
                PLow = x 
            
            if (x - PLow) > (high - low):
                low = PLow 
                high = x 

        print(PLow, low, high)
        return max(high - low, 0)
            
            
            
            
                
            



s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))

# Runtime: 1520 ms, faster than 58.23% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.1 MB, less than 38.55% of Python3 online submissions for Best Time to Buy and Sell Stock.
