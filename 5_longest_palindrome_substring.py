class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = None
        lpsub = s[0]
        for i in range(len(s)):
            letter = s[i]
            start = i
            for j in range(i + 1, len(s)):
                if letter == s[j]:
                    if (s[i:j+1] == s[j:i-1:-1] or
                        s[i:j+1] == s[j::-1]): # In case of the first element
                        end = j + 1
            if end != None:
                test_lps = s[start:end]
                if len(test_lps) > len(lpsub):
                    lpsub = test_lps

        return lpsub


if __name__ == '__main__':
    s = 'babad'
    sol = Solution()
    print(sol.longestPalindrome(s))
    s = 'cbbd'
    print(sol.longestPalindrome(s))
    s = "xycbcbc"
    print(sol.longestPalindrome(s))
    s = "cbbcxyziaeo"
    print(sol.longestPalindrome(s))
    s = "aacabdkacaa"
    print(sol.longestPalindrome(s))