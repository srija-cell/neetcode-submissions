# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#using inorder traversal for this as we can sort array and extract the k value of k

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node):
            if not node:
                return []
            left = inorder(node.left)
            parent = [node.val]
            right = inorder(node.right)
            return left + parent + right

        if not root:
            return []
        smallest_element = inorder(root)
        print(smallest_element)
        return smallest_element[k-1]
        