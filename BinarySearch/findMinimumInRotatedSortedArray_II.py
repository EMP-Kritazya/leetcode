class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        while l<r:
            m = l + ((r-l)//2)
            
#             Handle Simple Search First
            if nums[m] > nums[r]:
                l = m+1
                
            elif nums[m] < nums[r]:
                r = m
                
#             When mid and right are equal, we do:
#               1. Traverse the array of numbers left and check left neighboring element
            else:
                while r>0 and nums[r] == nums[r-1]:
                    r-=1
                if r>0 and nums[r-1] < nums[r]:
                    r = r - 1
                else:
                    return nums[r]
                    
        return nums[l]