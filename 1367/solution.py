from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if self._traverse(root, head):
            return True
        if not root:
            return False
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def _traverse(self, node, head: ListNode):
        if head is None:
            return True
        if node is None:
            return False
        if node.val == head.val:
            return self._traverse(node.left, head.next) or self._traverse(node.right, head.next)
        else:
            return False
