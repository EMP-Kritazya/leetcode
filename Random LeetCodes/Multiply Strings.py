class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        first = second = 0
        mul1, mul2 = (10**(len(num1)-1)), (10**(len(num2)-1))

        # find the ascii and then add
        for i in num1:
            temp = ord(i) - ord('0')
            first = (temp*mul1) + first
            mul1//=10
        
        for j in num2:
            temp = ord(j) - ord('0')
            second = (temp*mul2) + second
            mul2//=10
        
        return str(first*second)