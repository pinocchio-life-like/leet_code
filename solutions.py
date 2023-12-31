
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

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorderTraversal(root):
    if root is None:
        return []

    stack, output = [root, ], []

    while stack:
        root = stack.pop()
        if root is not None:
            output.insert(0, root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)

    return output

def searchRange(nums, target):
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return left if nums[left] == target else -1

    first, last = findFirst(nums, target), findLast(nums, target)
    return [first, last] if first != -1 else [-1, -1]

def searchRange(nums, target):
    if not nums:
        return [-1, -1]

    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return left if nums[left] == target else -1

    first, last = findFirst(nums, target), findLast(nums, target)
    return [first, last] if first != -1 else [-1, -1]


def isValidSudoku(board):
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    boxes = [{} for i in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                num = int(num)
                box_index = (i // 3 ) * 3 + j // 3

                rows[i][num] = rows[i].get(num, 0) + 1
                columns[j][num] = columns[j].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                    return False
    return True

def countAndSay(n):
    if n == 1:
        return "1"

    prev = countAndSay(n - 1)
    result = ""
    i = 0

    while i < len(prev):
        count = 1
        while i + 1 < len(prev) and prev[i] == prev[i + 1]:
            i += 1
            count += 1
        result += str(count) + prev[i]
        i += 1

    return result

def combinationSum(candidates, target):
    def backtrack(remain, comb, start):
        if remain == 0:
            result.append(list(comb))
            return
        elif remain < 0:
            return
        for i in range(start, len(candidates)):
            comb.append(candidates[i])
            backtrack(remain - candidates[i], comb, i)
            comb.pop()

    result = []
    backtrack(target, [], 0)
    return result

def combinationSum2(candidates, target):
    def backtrack(remain, comb, start):
        if remain == 0:
            result.append(list(comb))
            return
        elif remain < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            comb.append(candidates[i])
            backtrack(remain - candidates[i], comb, i + 1)
            comb.pop()

    candidates.sort()
    result = []
    backtrack(target, [], 0)
    return result

import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    head = point = ListNode(0)
    q = []

    for l in lists:
        if l:
            heapq.heappush(q, (l.val, l))

    while len(q) > 0:
        val, node = heapq.heappop(q)
        point.next = ListNode(val)
        point = point.next
        node = node.next
        if node:
            heapq.heappush(q, (node.val, node))

    return head.next

def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            transposed[c][r] = matrix[r][c]
    return transposed

from collections import Counter

def findSpecialInteger(arr):
    threshold = len(arr) // 4
    counter = Counter(arr)
    for num, count in counter.items():
        if count > threshold:
            return num
    return -1

import heapq

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_ratings = {food: -rating for food, rating in zip(foods, ratings)}
        self.cuisine_foods = {}
        for food, cuisine in zip(foods, cuisines):
            if cuisine not in self.cuisine_foods:
                self.cuisine_foods[cuisine] = []
            heapq.heappush(self.cuisine_foods[cuisine], (self.food_ratings[food], food))

    def changeRating(self, food, newRating):
        oldRating = self.food_ratings[food]
        self.food_ratings[food] = -newRating
        for cuisine in self.cuisine_foods:
            if food in [f for _, f in self.cuisine_foods[cuisine]]:
                self.cuisine_foods[cuisine].remove((oldRating, food))
                heapq.heapify(self.cuisine_foods[cuisine])
                heapq.heappush(self.cuisine_foods[cuisine], (self.food_ratings[food], food))

    def highestRated(self, cuisine):
        while self.cuisine_foods[cuisine] and self.cuisine_foods[cuisine][0][0] != self.food_ratings[self.cuisine_foods[cuisine][0][1]]:
            heapq.heappop(self.cuisine_foods[cuisine])
        return self.cuisine_foods[cuisine][0][1]
    
import heapq

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_ratings = {food: -rating for food, rating in zip(foods, ratings)}
        self.cuisine_foods = {}
        for food, cuisine in zip(foods, cuisines):
            if cuisine not in self.cuisine_foods:
                self.cuisine_foods[cuisine] = []
            heapq.heappush(self.cuisine_foods[cuisine], (self.food_ratings[food], food))

    def changeRating(self, food, newRating):
        self.food_ratings[food] = -newRating
        for cuisine in self.cuisine_foods:
            if food in [f for _, f in self.cuisine_foods[cuisine]]:
                heapq.heappush(self.cuisine_foods[cuisine], (self.food_ratings[food], food))

    def highestRated(self, cuisine):
        while self.cuisine_foods[cuisine] and self.cuisine_foods[cuisine][0][0] != self.food_ratings[self.cuisine_foods[cuisine][0][1]]:
            heapq.heappop(self.cuisine_foods[cuisine])
        return self.cuisine_foods[cuisine][0][1]
    
    
#Minimum Time to Make Rope Colorful  
class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        if len(colors) == 0 or len(colors) == 1:
                return 0

        time_count = 0
        color = colors[:2]
        time = neededTime[:2]

        i=0
        while len(color) > 1:
            t1 = time[0]
            t2 = time[1]
            if color[0] == color[1]:
                if t1<t2:
                    time_count += t1
                else:
                    neededTime[i+1] = t1
                    time_count += t2
                        
            i+=1

            color = colors[i:i+2]
            time = neededTime[i:i+2]
        return time_count