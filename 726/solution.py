import re
from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        eles = re.findall(r"[A-Z][a-z]*|\d+|\(|\)", formula)
        c = Counter()
        multipliers = [1]
        brackets = 0
        coupled = False
        for idx in range(len(eles) - 1, -1, -1):
            if eles[idx].isnumeric():
                multipliers.append(int(eles[idx]))
                coupled = True
            elif eles[idx].isalpha():
                mult = 1
                for i in range(brackets + int(coupled)):
                    try:
                        mult *= multipliers[-i - 1]
                    except IndexError:
                        break
                c[eles[idx]] += mult
                if coupled:
                    multipliers.pop()
                coupled = False
            elif eles[idx] == ")":
                brackets += 1
                coupled = False
            elif eles[idx] == "(":
                brackets -= 1
                multipliers.pop()
                coupled = False

            if not multipliers:
                multipliers.append(1)
        res = ""
        for ele, count in sorted(c.items()):
            res += ele
            if count > 1:
                res += str(count)
        return res


if __name__ == "__main__":
    Solution().countOfAtoms("Mg((AB)3(CD)2)2")
    Solution().countOfAtoms("HaH2O3")
    Solution().countOfAtoms("Mg(OH)2")
    Solution().countOfAtoms("K4(ON(SO3)2)2")
