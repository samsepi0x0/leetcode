# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def node(val, left, right):
            """
                Create a node and return after assigning left and right to the node.
            """
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node
        def trees(first, last):
            """
                create nodes in range 1..n, and recursively assign left and right in the trees (left side=1--root-1 and right side root+1--n) 
            """
            return [node(root, left, right) for root in range(first, last+1) for left in trees(first, root-1) for right in trees(root+1, last)] or [None]
        return trees(1, n)
