class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)-1
        
        while l<r:
            m = l+((r-l)//2)
            
            if letters[m] == target:
                
                # letters might contains series of same target and greater letter at the end
                # so if we look right and find greater than target we return it else we decrease
                # our search space
                
                if m+1 <= len(letters)-1 and letters[m+1] > target:
                    return letters[m+1]
                else:
                    l = m + 1
            elif letters[m] > target:
                r = m
            
            else:
                l = m + 1
        
        if letters[l] > target:
            return letters[l]
        else:
            return letters[0]