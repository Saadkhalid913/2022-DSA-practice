from __future__ import annotations
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        numCoins = len(coins)
        coinNums = [
            [0 for i in range(n)] for i in range(numCoins)
        ]

        for i in range(numCoins):
            for j in range(n):
                if j == 0:
                    coinNums[i][j] = 0
                
                
                



S = Solution()
print(S.coinChange([1,2,5], 11))