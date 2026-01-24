class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s = "".join([i for i in s if i.isalnum()])
        new_s = s[::-1]

        # now since new_s is reversed we can enumerate, with index i to check in s and value n to check in new_s
        for i,n in enumerate(new_s):
            if n != s[i]:
                return False
        
        return True