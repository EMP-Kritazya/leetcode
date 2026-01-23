class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,1

        while j<=len(nums)-1:
            if nums[i] == 0:
                while j<=len(nums)-1 and nums[j]==0:
                    j+=1
                
                if j>len(nums)-1:
                    break
                
                nums[i], nums[j] = nums[j], nums[i]

            i+=1
            j+=1