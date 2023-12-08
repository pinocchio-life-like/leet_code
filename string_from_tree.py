def tree2str(root):
    """
    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return ""

    left = tree2str(root.left)
    right = tree2str(root.right)

    if left == "" and right == "":
        return str(root.val)
    if right == "":
        return str(root.val) + '(' + left + ')'
    return str(root.val) + '(' + left + ')' + '(' + right + ')'
