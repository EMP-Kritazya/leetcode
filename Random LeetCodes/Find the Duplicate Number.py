class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         This works but the requirement of using constant extra space cannot be full filled
#         hashSet = set()
        
#         for i in nums:
#             if i in hashSet:
#                 return i
#             hashSet.add(i)

#       To tackle constant extra space, we make use of folyd's algorithm
        
        slowPtr = 0
        fastPtr = 0
        
        # we loop till fastPtr and slowPtr meet
        while (1):
            slowPtr = nums[slowPtr]
            fastPtr = nums[nums[fastPtr]]

            if(fastPtr == slowPtr):
                break
                
        # now we define another slow pointer
        # both slow pointers are gonna move till they meet and once they meet return the value
        slowPptr = 0
        
        while (1):
            slowPtr = nums[slowPtr]
            slowPptr = nums[slowPptr]
            
            if(slowPptr == slowPtr):
                return slowPptr

        return None
    
            
            