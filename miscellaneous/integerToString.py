'''
Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 2^31 - 1.
'''

class Solution:
    def getTwoWord(self, num, words):
        output = ''
        if len(num) == 1:
            return words[1][int(num[0])]
        if int(num) <= 20:
            output += words[int(num)]
        else:
            count = 0
            x, y = 2, 1
            output += words[x][int(num[count])]
            count += 1
            if not int(num[count]) == 0:
                output += words[y][int(num[count])]
        return output

    def getThreeWord(self, num, words):
        output = ''
        x, y, z = 3, 2, 1
        count = 0
        if not int(num[count]) == 0:
            output += words[z][int(num[count])] + words[x][0]
        count += 1

        if int(num[count]) == 1:
            output += self.getTwoWord(num[1:], words)
            return output
        elif not int(num[count]) == 0:
            output += words[y][int(num[count])]
        count += 1

        if not int(num[count]) == 0:
            output += words[z][int(num[count])]
        return output

    def numberToWords(self, num: int) -> str:
        stack = [' Billion', ' Million', ' Thousand', '']
        words = {
                1:[' Zero', ' One', ' Two', ' Three', ' Four',
                   ' Five', ' Six', ' Seven', ' Eight', ' Nine'],
                2:[' *', ' *', ' Twenty', ' Thirty', ' Forty',
                   ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety'],
                3:[' Hundred'], 10: ' Ten', 11:' Eleven', 12:' Twelve',
                13:' Thirteen', 14: ' Fourteen',15:' Fifteen', 16:' Sixteen',
                17:' Seventeen', 18:' Eighteen', 19:' Nineteen', 20:' Twenty'
                }

        nums = str(num)
        res = ''
        remaining = ''

        for i in range(len(nums), -1, -3):
            temp = nums[i-3:i]
            if len(temp) == 3:
                if int(temp) == 0:
                    stack.pop()
                else:
                    res = self.getThreeWord(nums[i-3:i], words) + stack.pop() + res
            else:
                remaining = nums[:i]
        if remaining:
            res = self.getTwoWord(remaining, words) +stack.pop() + res
        return res.strip()

num = 1790001
s = Solution()
print(s.numberToWords(num))
