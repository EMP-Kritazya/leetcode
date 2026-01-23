class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = 0
        trav = len(arr)-1

        #Logic:
            # traverse the array in reverse
            # keep storing the largest element in greatest variable
            # When encountering an element if it is greater than greatest replace it with greatest
                # and change the greatest to that element
            # Else, just replace the element
        
        while trav>=0:
            if trav!=len(arr)-1:
                if arr[trav]>greatest:
                    arr[trav], greatest = greatest, arr[trav]
                else:
                    arr[trav] = greatest
            else:
                greatest = arr[trav]
            trav-=1
        
        arr[-1] = -1

        return arr
            

                
                