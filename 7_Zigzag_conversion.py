class Solution:
    def convert(self, s, numRow):
        matrix = [[] for _ in range(numRow)]
        idx = 0
        m_idx = 0
        reverse = False
        while idx < len(s):
            if not reverse:
                matrix[m_idx].append(s[idx])
                m_idx += 1
                if m_idx == numRow:
                    m_idx -= 2
                    reverse = True
            else:
                matrix[m_idx].append(s[idx])
                m_idx -=1
                if m_idx < 0:
                    m_idx += 2
                    reverse = False
            idx += 1

        return ''.join([char for row in matrix for char in row])


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRow = 3
    sol = Solution()
    print(sol.convert(s, numRow))
    s = "PAYPALISHIRING"
    numRow = 4
    print(sol.convert(s, numRow))