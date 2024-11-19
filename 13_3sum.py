class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the list first
        lst = []  # List to store the triplets

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # Skip duplicates
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    lst.append([nums[i], nums[left], nums[right]])
                    # Move the pointers to skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return lst


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4] # [-4, -1, -1, 0, 1, 2]
    sol = Solution()
    print(sol.threeSum(nums))
    nums = [-2,0,1,1,2]
    print(sol.threeSum(nums))
    nums = [0, 0, 0, 0]
    print(sol.threeSum(nums))