# Chapter 18 Advanced topics

> page 632 in book

## 18.2. Topological sort

This is a way of ordering the list of nodes such that if `(a, b)` is an edge in the graph, then `a` will appear before `b` in the list. If a graph has cycles or isn't directed, then there's no topological sort.

Applications: if a graph represents parts on an assembly line. The edge (Handle, Door) indicates that you need to assemble the handle before the door. The topological sort would offer a valid ordering for the assembly line.

1. Identify all nodes with no incoming edges and add those nodes to the topological sort
   1. Those nodes can be added first because they have nothing that needs to come before them
   2. Such a node must exist if there's no cycle. If we picked an arbitrary node, we could just walk edges backwards arbitrarily. We either stop at some point (in which case we've found a node with no incoming edges), or we return to a prior node (there's a cycle)
2. After that, remove each node's outbound edges from the graph
   1. Those nodes have already been added to the sort, so they're irrelevant. We can't violate those edges anymore
3. Repeat the above, adding nodes with no incoming edges and removing their outbound edges. We finish when all nodes are added to the sort.

More formally, the algorithm works like this:

1. Create a queue `order`, which eventually stores the valid topological sort. Empty at the beginning
2. Create a queue `processNext`, which stores the next nodes to process
3. Count the number of incoming edges of each nodes to set a class variable `node.inbound`. Nodes typically only store their outgoing edges. But we can count the inbound edges by walking through each node `n` and, for each of its outgoing edges (n, x), incrementing `x.inbound`.
4. Walk through the nodes again and add to `processNext` any node where `x.inbound` == 0
5. While `processNext` not empty:
   1. Remove first node `n` from `processNext`
   2. For each edge (n, x), decrement `x.inbound`. If `x.inbound` == 0, append `x` to `processNext`
   3. Append `n` to `order`
6. If `order` contains all the nodes, success. Otherwise, the topological sort has failed due to a cycle.

## 18.4. Hash table collision resolution

Collision in a hash table means there's already an item stored at the designated index.

### 18.4.1. Chaining with linked lists

The hash table's array maps to a linked list of items, items are just added to the linked list. As long as the number of collisions is fairly small, this is quite efficient. In the worst case, runtime is O(n), where n = \# elements in the hash table. This would only happen with strange data or a very poor hash function, or both.

### 18.4.2. Chaining with binary search trees

Rather than storing collisions in a linked list, store them in a binary search tree. The worst case runtime is then O(logn). This approach isn't used unless we expect a very nonuniform distribution.

### 18.4.3. Open addressing with linear probing

When a collision occurs, we move on to the next index in the array until we find an open spot, or sometime, some other fixed distance, such as idx + 5. If the \# collisions is low, this is very fast and space-efficient. A drawback is that the total \# entries in the hash table is limited by the size of the array, which isn't the case with chaining.

Another issue called *clustering*, a hash table with an underlying array of size 100, where only indexes 20-29 are filled. The odds of the next insertion going to index 30 is 10%, since any item mapped to 20-30 will end up at index = 30.

### 18.4.4. Quadratic probing and double hashing

The distance between probes doesn't have to be linear, it can be quadratic, or use another hash function to determine the probe distance.

## 18.5. Rabin-Karp substring search

Searching for a substring S in a bigger string B, brute force approach takes O(s(b-s)) time, by searching through the first b - s + 1 characters in B and for ech, checking if the next s characters match S.

If two strings are the same, they must have the same hash. But it's also possible for two different strings to have the same hash. If we efficiently precompute a hash value for each sequence of s characters within B, we can find the location of S in O(b) time. For example, hash function is sum of each character. The substring S has value of 24 for example. We go through the string B, check how many times the sum of characters is 24, and check which one (if any) are indeed equal to S.

How to compute the hash value? If we calculate hash value of each substring, that still takes O(s(b-s)). Instead, we know that hash(s[1:4]) = hash(s[:3]) - code(s[0]) + code(s[4]). This takes O(b) time.
