class Solution:
    def longestCommonPrefix(self, strs):
        val = strs[0]
        for i in range(1, len(strs)):
            if strs[i] == "":
                return ""
            for j in range(len(strs[i])):
                if j < len(val):
                    if val[j] != strs[i][j]:
                        val = val[:j]
                        break
                if j == len(strs[i]) - 1:
                    val = val[:j + 1]
        return val

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))
    strs = ["dog","racecar","car"]
    print(sol.longestCommonPrefix(strs))
    strs = ["ab","a"]
    print(sol.longestCommonPrefix(strs))