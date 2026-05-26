class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        area = 0

        while start<end:
            h1 = height[start]
            h2 = height[end]
            gap = end - start
            temp = min(h1, h2)*gap

            if temp>area:
                area = temp

            if h1<h2:
                start+=1
            else:
                end-=1
        
        return area
            