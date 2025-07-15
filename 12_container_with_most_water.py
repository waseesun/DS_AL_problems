class Solution:
    def maxArea(self, height):
        max_start_idx = 0
        max_end_idx = len(height) - 1
        start_idx = 0
        end_idx = len(height) - 1
        max_val = 0
        while start_idx < end_idx:
            if height[max_start_idx] < height[max_end_idx]:
                temp_val = height[max_start_idx] * (max_end_idx - max_start_idx)
                if temp_val > max_val:
                    max_val = temp_val
                max_start_idx += 1
                start_idx += 1
            elif height[max_end_idx] < height[max_start_idx]:
                temp_val = height[max_end_idx] * (max_end_idx - max_start_idx)
                if temp_val > max_val:
                    max_val = temp_val
                max_end_idx -=1
                end_idx -= 1
            else:
                if height[max_end_idx] == height[max_start_idx]:
                    temp_val = height[max_end_idx] * (max_end_idx - max_start_idx)
                    if temp_val > max_val:
                        max_val = temp_val
                    max_start_idx += 1
                    max_end_idx -= 1
                start_idx += 1
                end_idx -= 1

        return max_val

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    print(s.maxArea([1,1]))
    print(s.maxArea([1,2,4,3]))

