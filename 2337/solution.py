class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s_idx = 0
        s_l = len(start)
        for t_idx, t in enumerate(target):
            match t:
                case "_":
                    continue
                case "L":
                    for search in range(s_idx, s_l):
                        match start[search]:
                            case "R":
                                return False
                            case "L":
                                if search < t_idx:
                                    return False
                                s_idx = search + 1
                                break
                            case "_":
                                continue
                    else:
                        return False
                case "R":
                    for search in range(s_idx, s_l):
                        match start[search]:
                            case "R":
                                if search > t_idx:
                                    return False
                                s_idx = search + 1
                                break
                            case "L":
                                return False
                            case "_":
                                continue
                    else:
                        return False
        for leftover in range(s_idx, s_l):
            match start[leftover]:
                case "_":
                    continue
                case _:
                    return False
        return True


if __name__ == "__main__":
    start = "_L__R__R_"
    target = "L______RR"
    print(Solution().canChange(start, target))
