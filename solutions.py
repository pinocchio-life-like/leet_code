
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    
    return root



def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def check_height(node):
        if node is None:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
    
    return check_height(root) != -1

def hasPathSum(root, targetSum):
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == targetSum
    
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


def generate(numRows):
    triangle = []

    for row_num in range(numRows):
        # The first and last row elements are always 1.
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, len(row)-1):
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

        triangle.append(row)

    return triangle


def getRow(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0]+row, row+[0])]
    return row

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

def isPalindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next

    return True

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorderTraversal(root):
    if root is None:
        return []

    stack, output = [root, ], []

    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

    return output

