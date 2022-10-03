class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_1 =list()
        carry = 0
        x = digits[-1] + 1
        if x == 10:
            x = 0
            carry = 1
        digits_1.append(x)
        for i in range(len(digits)-2, -1, -1):
            #print(digits[i])
            x = digits[i] + carry
            if x == 10:
                x = 0
                carry = 1
            else:
                carry = 0
            digits_1.append(x)
        if carry == 1:
            digits_1.append(carry)
        return digits_1[::-1]
        
