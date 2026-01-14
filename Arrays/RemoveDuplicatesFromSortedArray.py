class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = k = count = temp = 0
        while i < len(nums):
            if (nums[i] != temp or i == 0):
                nums[k] = nums[i]
                temp = nums[k]
                k+=1
                count +=1

            i+=1
        return count