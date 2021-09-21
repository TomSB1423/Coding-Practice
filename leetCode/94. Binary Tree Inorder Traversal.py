# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []

        def say(root):
            if root != None:
                if root.left:
                    say(root.left)
                order.append(root.val)
                if root.right:
                    say(root.right)
                return
        say(root)
        return order
