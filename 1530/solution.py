from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.distance = distance
        self.res = 0
        self.traverse(root)
        return self.res

    def traverse(self, node) -> Optional[dict]:
        if node:
            left = self.traverse(node.left)
            right = self.traverse(node.right)
        else:
            return None
        if left and right:
            self.res += self.good_nodes(left, right)
            return {k + 1: left.get(k, 0) + right.get(k, 0) for k in set(left) | set(right)}
        if left:
            return {k + 1: v for k, v in left.items()}
        if right:
            return {k + 1: v for k, v in right.items()}
        if left is None and right is None:
            return {1: 1}

    def good_nodes(self, left, right):
        res = 0
        for lk, lv in left.items():
            if lk > self.distance:
                continue
            for rk in range(self.distance - lk):
                res += lv * right.get(rk + 1, 0)
        return res


if __name__ == "__main__":
    print(
        Solution().countPairs(
            TreeNode(
                1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, TreeNode(6), TreeNode(7)),
            ),
            8,
        )
    )
