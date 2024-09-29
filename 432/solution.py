from collections import defaultdict


class AllOne:

    def __init__(self):
        self.strings = defaultdict(int)
        self.counts = defaultdict(set)

    def inc(self, key: str) -> None:
        old_count = self.strings[key]
        self.strings[key] += 1
        if old_count != 0:
            if len(self.counts[old_count]) == 1:
                self.counts.pop(old_count)
            else:
                self.counts[old_count].remove(key)
        self.counts[old_count + 1].add(key)

    def dec(self, key: str) -> None:
        old_count = self.strings[key]
        self.strings[key] -= 1
        if len(self.counts[old_count]) == 1:
            self.counts.pop(old_count)
        else:
            self.counts[old_count].remove(key)
        if old_count > 1:
            self.counts[old_count - 1].add(key)

    def getMaxKey(self) -> str:
        if not self.counts:
            return ""
        return next(iter(self.counts[max(self.counts.keys())]))

    def getMinKey(self) -> str:
        if not self.counts:
            return ""
        return next(iter(self.counts[min(self.counts.keys())]))


if __name__ == "__main__":
    obj = AllOne()
    obj.inc("hello")
    obj.inc("hello")
    print(obj.getMaxKey())
    print(obj.getMinKey())
    obj.inc("leet")
    print(obj.getMaxKey())
    print(obj.getMinKey())
