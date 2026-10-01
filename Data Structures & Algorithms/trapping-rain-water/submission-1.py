class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        left = 0
        for i in range(len(height)):
            max_left[i] = left
            left = max(left, height[i])
  
        right = 0    
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = right
            right = max(right, height[i])
        
        water = 0
        for i in range(len(height)):
            add = min(max_left[i], max_right[i]) - height[i]
            if add < 0:
                add = 0
            water += add
        return water 
