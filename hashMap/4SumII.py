class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        count = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dict1[nums1[i]+nums2[j]]+=1
        
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                dict2[nums3[i]+nums4[j]]+=1
        
        for i in dict1:
            if 0-i in dict2:
                count += dict1[i]*dict2[0-i]
                  
        return count