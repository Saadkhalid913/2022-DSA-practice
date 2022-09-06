'''
Link: https://leetcode.com/problems/climbing-stairs/

'''
class Solution(object):
    
    def __init__(self):
        self.memo = {
            0: 1,
            1: 1
        }
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.memo.has_key(n):
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            
            return self.memo[n]
            
            
            
        