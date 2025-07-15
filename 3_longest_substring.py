class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        main = ''
        curr = ''
        for i in range(len(s)):
            if s[i] not in curr:
                curr += s[i]
            else:
                for j in range(len(curr) - 1, -1, -1):
                    if curr[j] == s[i]:
                        curr = curr[j+1:] + s[i]
                        break
                
            if len(main) <= len(curr):
                main = curr

        return len(main)
    
    
if __name__ == '__main__':
    s = 'dvdf'
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))