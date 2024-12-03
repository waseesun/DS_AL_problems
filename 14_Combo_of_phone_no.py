class Solution:
    number_map = {
        '1': [''],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '*': ['*'],
        '0': [' '],
        '#': ['#'],
    }

    def letterCombinations(self, digits):
        if digits == '':
            return []

        result = []

        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(''.join(current_combination))
                return

            current_digit = digits[index]
            letters = self.number_map[current_digit]

            for letter in letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()

        backtrack(0, [])

        return result


if __name__ == '__main__':
    digits = '275'
    sol = Solution()
    print(sol.letterCombinations(digits))
