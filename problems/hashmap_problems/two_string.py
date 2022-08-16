'''
Given two strings, determine if they share a common substring. A substring may be as small as one character.

LINK: https://www.hackerrank.com/challenges/two-strings/problem

'''


## approach:
## consider the set of all common substrings between strings A and B. Lets choose a substring S from that set. Any letter in S will
## be in the set of common substrings between A and B, and will therefore be in the set. 
## we can simplify our algorithm to therefore only check for common letters 


#!/bin/python3



## HACKERANK CODE 

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#



## MY SOLUTION
def twoStrings(a, b):
    letters = dict()
    if len(a) < len(b):
        for char in a:
            letters[char] = True

        for char in b:
            if char in letters:
                return "YES"  
    else:
        for char in b:
            letters[char] = True

        for char in a:
            if char in letters:
                return "YES"
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2) 

        fptr.write(result + '\n')

    fptr.close()
