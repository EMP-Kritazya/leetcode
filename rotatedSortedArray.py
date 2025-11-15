class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r  = 0, len(nums)-1

        return self.findIndex(nums, l, r, target)
    
    def findIndex(self, nums, left, right, target):
        if left == right:
            if nums[left] == target:
                return left
            else:
                print(left)
                print(nums[left])
                return -1
        
        if left>right:
            return -1
        
        mid = left + ((right-left)//2)

        if nums[left]<=nums[mid]:
            if nums[mid] > target and nums[left]<=target:
                return self.findIndex(nums, left, mid-1, target)
            elif (target < nums[mid] and nums[left]>target) or (nums[mid] < target):
                return self.findIndex(nums, mid+1, right, target)
            else:
                return mid
        
        else:
            if (nums[mid] < target and nums[right] < target) or (nums[mid] > target):
                return self.findIndex(nums,left, mid-1, target)
            elif nums[mid] < target and nums[right] >= target:
                return self.findIndex(nums, mid+1, right, target)
            else:
                return mid

s1 = Solution()

nums = [5,1,3]

ans = s1.search(nums, 3)

print(ans)
            