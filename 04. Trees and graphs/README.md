# Chapter 4: Trees and graphs

In trees, the worst case and average case time may vary wildly, and we must evaluate both aspects of any algorithm. A tree is a type of graph.

## 1. Trees

A tree is a data structure composed of nodes. Each tree has a root node, the root node has 0+ child nodes (0 or more). Each child node has 0+ child nodes, and so on. The tree can't contain cycles. The nodes might be in a particular order, they can have any data type as values, and may or may not have links back to their parent roles.

A simple class definition for Node is:

```java
class Node {
    public String name;
    public Node[] children;
}
```

We can also have a Tree class to wrap this node, but it's not usually used:

```java
class Tree {
    public Node root;
}
```

### 1.1. Trees vs. binary trees

A binary tree is a tree in which each node has up to 2 children. A node is called a 'leaf' node if it has no children.

### 1.2. Binary tree vs. binary search tree

A binary tree is a binary tree in which every node fits a specific ordering property: `all left descendents <= n < all right descendents`. This must be true for each node n. Regarding equality, under some definitions, the tree can't have duplicate values, in others, the duplicate values will be on the right or can be on either side. All are valid definitions but it must be cleared out with the interviewer.

This inequality must be true for all of a node's descendents, not just its immediate children. This is a binary search tree:

* 8
  * 4
    * 2
    * 6
  * 10
    * 20

This is not a binary search tree, because `12` is bigger than `10`:

* 8
  * 4
    * 2
    * 12
  * 10
    * 20

### 1.3. Balanced vs. unbalanced

Trees don't necessarily need to be balanced. Balanced means being balanced enough to ensure O(nlogn) times for `insert` and `find`, but not necessarily as balanced as it can be. Two common types of balanced trees are red-black trees and AVL trees (chapter 11: advanced topics).

### 1.4. Complete binary trees

A complete binary tree is a binary tree in which every level of the tree is fully filled, except for perhaps the last level. To the extent that the last level is filled, it's filled left to right. A complete binary tree:

* 10
  * 5
    * 3
    * 7
  * 20
    * 15

Not a complete binary tree, because `30` is bigger than `20`:

* 10
  * 5
    * 3
    * 7
  * 20
    * 30

### 1.5. Full binary trees

A full binary tree is a binary tree in which every node has either 0 or 2 children. There are no nodes with only one child.

### 1.6. Perfect binary trees

A perfect binary tree is one that is both full and complete, all leaf nodes are at the same level, and this level has teh maximum number of nodes. 2^k-1 nodes in total:

* 10
  * 5
    * 9
    * 18
  * 20
    * 3
    * 7

## 2. Binary tree transversal

### 2.1. In-order transversal

This means visiting/printing the left branch, then the current node, and then right branch

```java
void inOrderTransversal(TreeNode node) {
    if (node != null) {
        inOrderTransversal(node.left);
        visit(node);
        inOrderTransversal(node.right);
    }
}
```
