class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        min_v, max_r = heights[0], heights[0]
        stack = [(min_v,0)]
        for i in range(1,len(heights)):
          if heights[i] > stack[-1][0]:
            stack.append((heights[i],i))
            
          elif heights[i] <= stack[-1][0]:
            hist, start = stack.pop()

            if max_r < (hist * (i - start)):
              max_r =  (hist * (i - start))
            while stack and heights[i] <= stack[-1][0]:
              hist, start = stack.pop()
              if max_r < (hist * (i - start)):
                max_r =  (hist * (i - start))
            stack.append((heights[i],start))

        while stack:
            hist, start = stack.pop()

            rect_area = hist * (len(heights) - start) 
            if max_r < rect_area:
              max_r = rect_area

        return max_r
