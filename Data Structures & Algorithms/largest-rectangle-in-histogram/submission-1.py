class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        area=0
        for i in range(len(heights)):
            left=i
            while stack and stack[-1][1]>heights[i]:
                area = max(area,stack[-1][1]*(i-stack[-1][0]))
                left = stack[-1][0]
                stack.pop()
            stack.append([left,heights[i]])
        i=len(heights)
        while stack:
            area = max(area,stack[-1][1]*(i-stack[-1][0]))
            stack.pop()
        return area