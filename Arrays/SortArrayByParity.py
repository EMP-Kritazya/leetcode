class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        first, last = 0, len(nums)-1
    
        while first<last:
            if nums[first]%2!=0:
                last = self.findLasteven(first, last, nums)
                if last==None:
                    return nums
                else:
                    nums[first], nums[last] = nums[last], nums[first]
                    last-=1
            first+=1
        return nums
    

    def findLasteven(self, first, last, nums):
        while first<last:
            if nums[last]%2 != 0:
                last-=1
            else:
                return last
        return None