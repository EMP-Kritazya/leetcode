class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for idx in range(len(s)):
            counter = 0
            left = 0
            right = 0
            temp = ''

            while ((idx+1 + right) <=len(s)-1) and s[idx+1 + right] == s[idx]:
                right +=1
            
            while ((idx-1 - left) >=0) and s[idx-1 -left] == s[idx]:
                left +=1

            while ((idx-counter-left)>=0) and ((idx+counter+right)<=len(s)-1) and s[idx- counter - left] == s[idx+ counter + right]:
                temp = s[idx-counter - left : idx+counter + right+1]
                
                if len(temp)>len(longest):
                    longest = temp
                counter += 1
        
        return longest