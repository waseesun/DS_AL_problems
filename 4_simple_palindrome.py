class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i = 0
        j = len(x) - 1
        while i < j:
            if (x[i] != x[j]):
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    x = 121
    sol = Solution()
    print(sol.isPalindrome(x))
    y = -121
    print(sol.isPalindrome(y))
    z = 10
    print(sol.isPalindrome(z))