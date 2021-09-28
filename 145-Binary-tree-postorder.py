# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out = []
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.postorder(root)
        return self.out
    def postorder(self, root: Optional[TreeNode]) -> None:
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            if root.val is not None:
                self.out.append(root.val)
