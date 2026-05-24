class Solution:
    # Thorough solution: creates dicts; doens't have space complexity of O(1)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     left_memo = {}

    #     for idx in range(len(nums)):
    #         if idx == 0:
    #             left_memo[idx] = 1
    #             continue
    #         left = left_memo[idx-1]
    #         left_memo[idx] = left*nums[idx-1]

    #     right_memo = {}

    #     for idx in range(len(nums)-1, -1, -1):
    #         if idx == len(nums)-1:
    #             right_memo[idx] = 1
    #             continue
            
    #         right = right_memo[idx+1]
    #         right_memo[idx] = right * nums[idx+1]
            
    #     answer = [0]*len(nums)
    #     for idx in range(len(nums)):
    #         answer[idx] = left_memo[idx]*right_memo[idx]
    #     return answer

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        prefix = 1
        for idx in range(len(nums)):
            res[idx]=prefix
            prefix *= nums[idx]
        
        suffix = 1
        for idx in range(len(nums)-1, -1, -1):
            res[idx] *= suffix
            suffix*=nums[idx]

        return res



