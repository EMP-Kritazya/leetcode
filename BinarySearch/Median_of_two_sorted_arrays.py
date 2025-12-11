class Solution:
    
    # Less effecient Code
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>=len(nums2):
            Larray = nums1
            Sarray = nums2
        else:
            Larray = nums2
            Sarray = nums1
        
        Marray = Larray
        
        for i in Sarray:
            Marray = self.merge(Marray, i)
        

        if len(Marray)%2 == 1:
            median_pos = (len(Marray))//2
            return Marray[median_pos]
        else:
            median_pos = (len(Marray))//2
            lIndex = median_pos-1
            hIndex = lIndex+1
            return ((Marray[lIndex] + Marray[hIndex])/2)
        
        
    
    
    def merge(self, container, target):
        l, r = 0, len(container)-1
        
        while l+1<r:
            m = l+((r-l)//2)
            
            if container[m] < target:
                l = m
            elif container[m] > target:
                r = m
            else:
                container.insert(m, target)
                return container
        
        if target > container[l]:
            if target < container[r]:
                container.insert(l+1, target)
            else:
                container.insert(r+1, target)
            return container
        else:
            if target > container[l]:
                container.insert(l+1, target)
            else:
                container = [target] + container
            return container
    
        return None
    