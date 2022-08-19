

// LINK: https://leetcode.com/problems/sum-of-two-integers/submissions/

class Solution {
public:
    int getSum(int x, int y) {

        if (y == 0) {
            return x;
        }
        
        unsigned carry = x & y;
        carry = carry << 1;
        x = x ^ y;
 
        
        return getSum(x, carry);
        
    }
};