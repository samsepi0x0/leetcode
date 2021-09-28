# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.preorder(root)
        return self.out
    def preorder(self, root: Optional[TreeNode]) -> None:
        if root is not None:
            if root.val is not None:
                self.out.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
