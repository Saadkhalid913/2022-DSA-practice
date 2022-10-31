'''

LINK: https://leetcode.com/problems/longest-palindromic-substring/submissions/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longest_start = 0 
        longest_end = 0
        
        n = len(s)
        
        for i,x in enumerate(s):
            l,r = i,i

            while l >=0 and r < n and s[r] == s[l]:
                if longest < r - l:
                    longest = r - l
                    longest_start = l
                    longest_end = r 
                r += 1
                l -=1 

            l,r = i,i + 1 
            while l >=0 and r < n and s[r] == s[l]:
                if longest < r - l:
                    longest = r - l
                    longest_start = l
                    longest_end = r 
                r += 1
                l -=1 
        
        
        return s[longest_start : longest_end + 1]
        
        
        
            
        