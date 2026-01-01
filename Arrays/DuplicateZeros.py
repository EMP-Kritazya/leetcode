class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # Efficient Solution O(n)
        num_zeros = arr.count(0)

        for i in range(len(arr)-1, -1, -1):
            if i+num_zeros < len(arr):
                arr[i+num_zeros] = arr[i]
            
            if arr[i] == 0:
                num_zeros-=1
                if i+num_zeros<len(arr):
                    arr[i+num_zeros] = 0
            

        
        # Ineffecient working way that I can currently think of
        # -- very straightforward -- O(n^2)
        i = 0
        traverse = 0
        hold = 0

        while i!=len(arr):
            if arr[i] == 0 and i<len(arr)-1:
                hold = arr[i+1]
                arr[i+1] = 0
                i+=2
                traverse = i

                while traverse<=len(arr)-1:
                    temp = arr[traverse]
                    arr[traverse] = hold
                    hold = temp
                    traverse+=1
            else:
                i+=1