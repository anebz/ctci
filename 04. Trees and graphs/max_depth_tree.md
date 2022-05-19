# Find Maximum depth of binary tree

[LeetCode problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

![ ](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

Example: input: [3,9,20,null,null,15,7], output: 3.

## LeetCode initial code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
```

## Recursive approach

Depth first

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    def max_depth(root, depth):
        if not root: return depth
        return max(max_depth(root.left, depth+1), max_depth(root.right, depth+1))
    
    return max_depth(root, 0)
```

## Iterative solution

Breadth first

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:

    if not root:
        return 0
    
    queue = [root]
    depth = 0

    while True:

        if not queue:
            break

        node_count = len(queue)
        depth += 1

        while node_count > 0:
            
            node = queue[0]
            queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            node_count -= 1

    return depth

```
