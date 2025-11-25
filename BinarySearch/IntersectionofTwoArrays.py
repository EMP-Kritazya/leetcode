class Solution:
# more efficient solution. Uses HashSets
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        hashSet = set(nums1)
        for i in nums2:
            if i in hashSet:
                output.append(i)
                hashSet.remove(i)
        
        return output


# Less efficient solution but is more efficient as compared to linear searching throughout the array
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        mini = nums1 if len(nums1)<len(nums2) else nums2
        maxi = nums1 if mini == nums2 else nums2
        mini.sort()
        maxi.sort()
        
        
        for i in mini:
            a = self.BinarySearch(i, maxi)
            if a!=-1 and a not in result:
                result.append(a)
        
        return result
        
    def BinarySearch(self, i, maxi):
        l, r = 0, len(maxi)-1
        
        while l < r:
            m = l + ((r-l)//2)
            
            if maxi[m] > i:
                r = m-1
            elif maxi[m]<i:
                l = m + 1
            else:
                maxi.pop(m)
                return i
        
        return i if maxi[l] == i else -1