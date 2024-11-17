class Solution:
    val_dict = {
        1 : "I",
        5 : "V",
        10 : "X",
        50 : "L",
        100 : "C",
        500 : "D",
        1000 : "M",
    }

    def conversion(self, temp_num, div):
        if temp_num < 4:
            return str(self.val_dict[div] * temp_num)
        elif temp_num == 4 or temp_num == 9:
            return f"{self.val_dict[div]}{self.val_dict[(temp_num+1) * div]}"
        elif 5 <= temp_num < 9:
            return f"{self.val_dict[5 * div]}{self.val_dict[div] * (temp_num-5)}"

    def intToRoman(self, num: int) -> str:
        val = ''
        while num != 0:
            temp_num = 0
            div = 1
            if len(str(num)) == 4:
                div = 1000
            if len(str(num)) == 3:
                div = 100
            if len(str(num)) == 2:
                div = 10
            temp_num = num // div
            num = num % div
            val += self.conversion(temp_num, div)

        return val

if __name__ == '__main__':
    num = 3749
    sol = Solution()
    print(sol.intToRoman(num))
    num = 58
    print(sol.intToRoman(num))
    num = 1994
    print(sol.intToRoman(num))






