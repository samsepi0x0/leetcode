/* //pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;
 IMPORTANT-->>
*** temp = rev x 10 + pop causes overflow then rev >= INTMAX/10
*** rev > INTMAX/10 then guranteed Overflow
*** if rev == INTMAX/10 then temp= revx 10 + pop will overflow if  pop > 7
*** if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8 */

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
*/

class Solution {
    public int reverse(int x) {
        int rev = 0;
        while(x!=0)
        {
           int pop = x % 10;
            x /= 10;
            // Overflow
            if(rev > Integer.MAX_VALUE/10 ||(rev == Integer.MAX_VALUE/10 && pop > 7))
                return 0;
            // UnderFlow
            if(rev < Integer.MIN_VALUE/10 ||(rev==Integer.MIN_VALUE/10 && pop < -8))
                return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
}

