import math


class Solution:
    def numberToWords(self, num: int) -> str:
        singles = {
            "0": "",
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine",
        }
        teens = {
            "10": "Ten",
            "11": "Eleven",
            "12": "Twelve",
            "13": "Thirteen",
            "14": "Fourteen",
            "15": "Fifteen",
            "16": "Sixteen",
            "17": "Seventeen",
            "18": "Eighteen",
            "19": "Nineteen",
        }
        deca = {
            "0": "",
            "2": "Twenty",
            "3": "Thirty",
            "4": "Forty",
            "5": "Fifty",
            "6": "Sixty",
            "7": "Seventy",
            "8": "Eighty",
            "9": "Ninty",
        }
        multi = {
            "0": "Hundred",
            "1": "Hundred",
            "2": "Thousand",
            "3": "Million",
            "4": "Billion",
        }

        s = list(reversed(str(num)))
        length = math.ceil(len(s) / 3)
        res = ""

        for i in range(length):
            subres = ""
            lower = 3 * i
            upper = 3 * (i + 1)
            sub = s[lower:upper]

            if len(sub) > 2 and sub[2] != "0":
                subres += singles[sub[2]] + " " + multi["0"]

            if len(sub) > 1:
                if len(sub) > 1 and sub[1] == "1":
                    subres += " " + teens["1" + str(sub[0])]
                else:
                    subres += " " + deca[sub[1]] + " " + singles[sub[0]]
            else:
                subres += " " + singles[sub[0]]
            subres += " " + multi[str(i)]
            res = subres + " " + res
        return res


if __name__ == "__main__":

    num = 12345
    s = Solution()
    print(s.numberToWords(num))
