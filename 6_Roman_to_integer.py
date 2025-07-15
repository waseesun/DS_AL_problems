class Solution:
    def romanToInt(self, s: str) -> int:
        val_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        val = 0
        for i in range(len(s)):
            if i < len(s) - 1:
                if val_dict[s[i]] < val_dict[s[i+1]]:
                    val -= val_dict[s[i]]
                    continue
            val += val_dict[s[i]]

        return val

if __name__ == '__main__':
    s = "MCMXCIV"
    sol = Solution()
    print(sol.romanToInt(s))