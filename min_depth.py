def minDepth(root):
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1
    
    min_depth = float('inf')
    
    if root.left:
        min_depth = min(min_depth, minDepth(root.left))
    
    if root.right:
        min_depth = min(min_depth, minDepth(root.right))
    
    return min_depth + 1

# if not root:
#             return 0
#         if not root.left and not root.right:
#             return 1
        
#         min_depth = float("inf")

#         if root.left:
#             min_depth = min(min_depth, self.minDepth(root.left))
#         if root.right:
#             min_depth = min(min_depth, self.minDepth(root.right)) 
        
#         return min_depth + 1