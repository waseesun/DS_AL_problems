class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        def backtrack(r, l, combo):
            if r == 3:
                r_sum = sum(combo)
                if r_sum == 0:
                    combo = [combo[0], combo[1], combo[2]]
                    if combo not in result:
                        result.append(combo)
                return

            for i in range(l, len(nums)):
                l += 1
                combo.append(nums[i])
                backtrack(r+1, l, combo)
                combo.pop()


        backtrack(0, 0, [])

        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4] # [-4, -1, -1, 0, 1, 2]
    sol = Solution()
    print(sol.threeSum(nums))
    nums = [-2,0,1,1,2]
    print(sol.threeSum(nums))
    nums = [0, 0, 0, 0]
    print(sol.threeSum(nums))