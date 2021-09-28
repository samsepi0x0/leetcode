# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        return self.out
    def inorder(self, root: Optional[TreeNode]) -> None:
        if root is not None:
            self.inorder(root.left)
            if root.val is not None:
                self.out.append(root.val)
            self.inorder(root.right)
