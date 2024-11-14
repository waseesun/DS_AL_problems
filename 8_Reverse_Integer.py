class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x = "-" + x[:0:-1]
        else:
            x = x[::-1]
        if -2**31 <= int(x) <= 2**31:
            return int(x)
        return 0


if __name__ == '__main__':
    x = 123
    sol = Solution()
    print(sol.reverse(x))
    x = -123
    print(sol.reverse(x))