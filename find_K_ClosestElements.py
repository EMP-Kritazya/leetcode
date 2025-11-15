class Solution:
    # Best solution
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0, len(arr)-k
        
        while l<r:
            m = l + ((r-l)//2)
            
            if x-arr[m] > arr[m+k] -x:
                l = m+1
            else:
                r = m

            
        return arr[l:l+k]
    
    # My solution    
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0, len(arr)-1

        # I need to binary search to find the closed value to x in the array
        while l<r:
            m = l + ((r-l)//2)
            if arr[m]>x:
                if m>0 and abs(arr[m]-x) > abs(arr[m-1]-x):
                    r = m-1
                elif arr[m] == arr[m-1]:
                    r = m - 1
                else:
                    r = m
            elif arr[m]<x:
                if m<len(arr)-1 and abs(arr[m]-x) > abs(arr[m+1]-x):
                    l = m + 1
                elif arr[m] == arr[m+1]:
                    l = m+1
                else:
                    r = m
            else:
                l = m
                break
        
        print(l)
        # l holds the index of the value that is closest to x in the array
        output = [arr[l]]

        ptr1 = l - 1
        ptr2 = l + 1
        for i in range(k-1):
            if ptr1>=0:
                if ptr2<=len(arr)-1:
                    # check if left value is closer to x
                    if abs(arr[ptr1]-x) < abs(arr[ptr2]-x):
                        output = [arr[ptr1]] + output
                        ptr1 = ptr1-1
                        
                    # check if right value is closer to x                        
                    elif abs(arr[ptr1]-x)>abs(arr[ptr2]-x):
                        output.append(arr[ptr2])
                        ptr2 = ptr2+1
                    
                    # else see what value is the smallest
                    else:
                        if arr[ptr1]<arr[ptr2]:
                            output = [arr[ptr1]] + output
                            ptr1 = ptr1-1
                        else:
                            output.append(arr[ptr2])
                            ptr2 = ptr2+1
                else:
                    output = [arr[ptr1]] + output
                    ptr1 = ptr1 - 1
            else:
                output.append(arr[ptr2])
                ptr2 = ptr2 + 1

        return output