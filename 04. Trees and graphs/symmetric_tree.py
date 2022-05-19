# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# checks if tree is symmetric
# https://leetcode.com/problems/symmetric-tree/

# recursive approach, depth first
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symm(root1, root2):
            
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            return symm(root1.left, root2.right) and symm(root1.right, root2.left)
            
        if not root:
            return True
        return symm(root.left, root.right)


# iterative approach, breadth first 
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            
        if not root:
            return True
        queue = [(root.left, root.right)]
        
        while True:

            if not queue:
                return True
            count = len(queue)

            while count > 0:

                root1, root2 = queue[0]
                queue.pop(0)

                if not root1 and not root2:
                    return True
                if not root1 or not root2 or root1.val != root2.val:
                    return False
                
                if root1.left or root2.right:
                    queue.append((root1.left, root2.right))
                if root1.right or root2.left:
                    queue.append((root1.right, root2.left))
                count -= 1
