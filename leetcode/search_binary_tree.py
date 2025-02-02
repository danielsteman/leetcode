# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        queue = [root]

        while queue:
            root = queue.pop(0)
            if root.val == val:
                return root

            if root.left:
                queue.append(root.left)

            if root.right:
                queue.append(root.right)

        return None


if __name__ == "__main__":
    print(Solution().searchBST(TreeNode(val=2), 2))
