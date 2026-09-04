# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current=root
        if not current:
            root=TreeNode(val)
            return root
        while current is not None:
            if current.val>val:
                if current.left is None:
                    current.left=TreeNode(val)
                    return root
                current=current.left
            else:
                if current.right is None:
                    current.right=TreeNode(val)
                    return root
                current=current.right
