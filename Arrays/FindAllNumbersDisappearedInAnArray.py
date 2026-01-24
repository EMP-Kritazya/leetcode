class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #logic
            # we take advantage of the size of the array, the elements that it contains, and the elements being positive
                # we are going to mark up the elements according to it's value by going to the index pointed by the value itself
            
        for i in nums:
            n = abs(i)-1
            nums[n] = -1 * abs(nums[n])

        k = 0
        for i,n in enumerate(nums):
            if n>0:
                nums[k] = i+1
                k+=1
        return nums[:k]

        