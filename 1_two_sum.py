class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
if __name__ == '__main__':
    nums = [2,5,5,11]
    target = 10
    sol = Solution()
    print(sol.twoSum(nums, target))
    # nums = [11]
    # print([str(nums[0])])