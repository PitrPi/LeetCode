from collections import Counter, defaultdict, deque


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        c = self.count_complex(formula)
        res = ""
        for key, value in sorted(c.items()):
            res += key
            if value > 1:
                res += str(value)
        return res

    def get_multiplicator(self, string):
        multiplicator = ""
        brackets = 1
        for s in string:
            if brackets == 0 and s.isnumeric():
                multiplicator += s
            elif s == "(" and multiplicator == "":
                brackets += 1
            elif s == ")" and multiplicator == "":
                brackets -= 1
            elif brackets == 0:
                break

        return int(multiplicator) if multiplicator else 1

    def count_complex(self, string: str) -> Counter:
        res = Counter()
        for idx, s in enumerate(string):
            if s == "(":
                res += self.count_simple(string[:idx])
                comple = self.count_complex(string[idx + 1 :])
                multiplicator = self.get_multiplicator(string[idx + 1 :])
                if comple:
                    for key, value in comple.items():
                        comple[key] = value * multiplicator
                    res += comple
                return res
            elif s == ")":
                simple = self.count_simple(string[:idx])
                # multiplicator = self.get_multiplicator(string[idx:])
                # for key, value in simple.items():
                #     simple[key] = value * multiplicator
                res += simple
                res += self.count_complex(string[idx + 1 :])
                return res
        return res

    def count_simple(self, string: str) -> Counter:
        c = Counter()
        c[""] = 0
        stack = ""
        latest = ""
        for idx, s in enumerate(string):

            if ord(s) >= 97:
                stack += s
            elif s.isnumeric():
                if stack.isnumeric():
                    stack += s
                else:
                    latest = stack
                    stack = s
            else:
                if stack.isnumeric():
                    c[latest] += int(stack)
                    stack = s
                else:
                    c[stack] += 1
                    stack = s
        if stack:
            if stack.isnumeric():
                c[latest] += int(stack)
            else:
                c[stack] += 1
        c.pop("")
        return c


if __name__ == "__main__":
    Solution().countOfAtoms("Mg((AB)3(CD)2)2")
    Solution().countOfAtoms("HaH2O3")
    Solution().countOfAtoms("Mg(OH)2")
