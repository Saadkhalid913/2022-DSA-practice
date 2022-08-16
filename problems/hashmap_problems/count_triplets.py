'''
LINK: https://www.hackerrank.com/challenges/count-triplets-1/problem

You are given an array and you need to find number of tripets of indices 
such that the elements at those indices are in geometric progression for 
a given common ratio and i < j < k.
'''

import math
import os
import random
import re
import sys

## worse solution
def countTripletsDebug(arr, r):
    count = 0
    lookup = dict()
    for i, val in enumerate(arr):
        if val not in lookup:
            lookup[val] = [i]
        else:
            lookup[val].append(i)
        
        if (val // r) in lookup and (val // (r ** 2)) in lookup:
            for q in lookup[val // r]:
                for w in lookup[val // (r**2)]:
                    if w < q < i:
                        count +=1 

## better solution
def countTriplets(arr, r):
    count = 0 #number of times we've seen L1 * R**2 
    
    allNums = {} # all numbers 
    L1Lookup = {} # number of times we've seen L1 * R 
    for val in reversed(arr):

        # if val * r is the second term in a sequence, then val is the first, so we increment count 
        # by the number of times we've seen val * r ahead of val
        if val * r in L1Lookup:
            count += L1Lookup[val * r]

        # if val * r has been seen, then val is the second term in a geometric sequence, therefore 
        # we increment its value in the L1 Lookup array by one (number of times we've seen a potential
        # 2nd element)

        if val * r in allNums:
            L1Lookup[val] = L1Lookup.get(val, 0) +  allNums[r * val]
        
        ## we add the value to allNums indiscriminantly 
        allNums[val] = allNums.get(val, 0) + 1 
    return count


if __name__ == '__main__':

    print(countTriplets([1, 5, 5, 25, 125], 5))
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nr = input().rstrip().split()

    # n = int(nr[0])

    # r = int(nr[1])

    # arr = list(map(int, input().rstrip().split()))

    # ans = countTriplets(arr, r)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
