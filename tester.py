# def test(n):
#     if n == 5:
#         return "Five "
#     else:
#         left = test(n-1)
#         return left + "Test "


# print(test(10))
haystack = "haystack"
stack = "stack"
print(haystack.index(stack))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.inorderHelper(root, result)
        return result
    
    def inorderHelper(self, node: TreeNode, result: List[int]):
        if node:
            self.inorderHelper(node.left, result)
            result.append(node.val)
            self.inorderHelper(node.right, result)
