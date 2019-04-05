# Chapter 11 Advanced topics

## 11.4. Hash table collision resolution

Collision in a hash table means there's already an item stored at the designated index.

### 11.4.1. Chaining with linked lists

The hash table's array maps to a linked list of items, items are just added to the linked list. As long as the number of collisions is fairly small, this is quite efficient. In the worst case, runtime is O(n), where n = \# elements in the hash table. This would only happen with strange data or a very poor hash function, or both.

### 11.4.2. Chaining with binary search trees

Rather than storing collisions in a linked list, store them in a binary search tree. The worst case runtime is then O(logn). This approach isn't used unless we expect a very nonuniform distribution.

### 11.4.3. Open addressing with linear probing

When a collision occurs, we move on to the next index in the array until we find an open spot, or sometime, some other fixed distance, such as idx + 5. If the \# collisions is low, this is very fast and space-efficient. A drawback is that the total \# entries in the hash table is limited by the size of the array, which isn't the case with chaining.

Another issue called *clustering*, a hash table with an underlying array of size 100, where only indexes 20-29 are filled. The odds of the next insertion going to index 30 is 10%, since any item mapped to 20-30 will end up at index = 30.

### 11.4.4. Quadratic probing and double hashing

The distance between probes doesn't have to be linear, it can be quadratic, or use another hash function to determine the probe distance.