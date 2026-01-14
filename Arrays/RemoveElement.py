class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # Easy Code
        # i = 0
        # while i<len(nums):
        #     if nums[i] == val:
        #         nums.pop(i)
        #     else:
        #         i+=1
        # return len(nums)
        
        ##
        
        # Detailed Logic

        count = 0
        #I'll try using two pointers logic
        i, j = 0, len(nums)-1

        while i<=j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                count+=1
                i+=1
        return count
    