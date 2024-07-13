class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        union_find_alice = UnionFind(n)
        union_find_bob = UnionFind(n)
        res = 0
        edges.sort(revese=True)
        for typ, start, end in edges:
            start, end = start - 1, end - 1
            if typ == 3:
                res += not (
                    union_find_alice.union(start, end)
                    and union_find_bob.union(start, end)
                )
            elif typ == 2:
                res += not union_find_bob.union(start, end)
            elif typ == 1:
                res += not union_find_alice.union(start, end)
        if union_find_alice.count == 1 and union_find_bob.count == 1:
            return res
        else:
            return -1


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [x for x in range(n)]
        self.rank = [1] * n

    def find(self, parent):
        if parent != self.parent[parent]:
            self.parent[parent] = self.find(self.parent[parent])
        return self.parent[parent]

    def union(self, p, q) -> bool:
        pr = self.find(p)
        qr = self.find(q)
        if pr == qr:
            return False
        self.count -= 1
        if self.rank[pr] > self.rank[qr]:
            pr, qr = qr, pr
        self.parent[pr] = qr
        self.rank[qr] += self.rank[pr]
        return True
