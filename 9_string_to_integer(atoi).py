class Solution:
    def myAtoi(self, s: str) -> int:
        val = ''
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            elif (s[i] == '+' or s[i] == '-') and val == '':
                val += s[i]
            elif not s[i].isdigit():
                break
            elif (s[i] == "0" and
                  i < len(s)-1 and
                  not s[i+1].isdigit()):
                break
            else:
                val += s[i]

        if val == '' or val == '+' or val == '-':
            return 0
        val = int(val)
        if val > 2**31-1:
            return 2**31-1
        elif val < -2**31:
            return -2**31
        else:
            return val

if __name__ == '__main__':
    s = "42"
    sol = Solution()
    print(sol.myAtoi(s))
    s = "   -42"
    print(sol.myAtoi(s))
    s = "1337c0d3"
    print(sol.myAtoi(s))
    s = "0-1"
    print(sol.myAtoi(s))
    s = "words and 987"
    print(sol.myAtoi(s))
    s = "21474836460"
    print(sol.myAtoi(s))

