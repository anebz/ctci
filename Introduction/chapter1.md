# Chapter 1

## 1.1. Big O

### 1.1. Time complexity

* Big O: upper bound on the time. if O(N), then O(N^2), O(N^3), etc
* Big Omega: lower bound. if omega(N), then omega(1), omega(logN)
* Big theta: an algorithm is big theta(N) if it's both O(N) and omega(N). theta gives a tight bound on runtime

Best case scenarios:

* Best case: with any algorithm, in a special case, we can make O(1)
* Worst case scenario: quick sort of a reverse ordered array, it might take O(N^2)
* Expected case: O(NlogN)

For most algorithms, the worst case and the expected case are the same.

### 1.2. Space complexity

Space complexity is a parallel concept to time complexity. Stack space in recursive calls counts, too.

```c
int sum(int n) { /* ex1 */
    if (n <= 0) {
        return 0;
    }
    return n + sum(n - 1);
}
```

This code takes O(n) time and O(n) space. in sum(4), there are 4 calls to the stack (sum(3), sum(2), sum(1), sum(0)).

```c
int pairSumSeq(int n) { /* ex2 */
    int sum = 0;
    for(int i=0; i < n; i++) {
        sum += pairSum(i, i+1);
    }
}
int pairSum(int a, int b) {
    return a + b;
}
```

`ex2` takes O(n) time complexity but O(1) space. There are O(n) calls to `pairSum`, but those calls don't happen simultaneously like in the recursive case of `ex1`.

### 1.3. Drop the constants

It's possible for O(N) code to run faster than O(1) code for specific inputs. Big O just describes the rate of increase, so we drop constants in runtime. O(2N) = O(N).

### 1.4. Drop the non-dominant terms

O(N^2 + N) = O(N^2)

### 1.5. Multi-part algorithms

In an algorithm with two steps, when to multiply runtimes and when to add?

* Add runtime: do A chunks of work, then B chunks of work

```c
for(int a: arrA) {
    print(a);
}
for(int b: arrB) {
    print(b);
}
```

* Multiply runtime: do B chunks of work for each element in A.

```c
for(int a: arrA) {
    for(int b: arrB) {
        print(a + ", " + b);
    }
}
```

### 1.6. Amortized time

With `ArrayList`s, when they reach full capacity, the class creates a new array with double the capacity and copy all the elements over to the new array. Say we want to add a new element to the `ArrayList`.

* If the array is full and contains N elements, adding a new element takes O(N) time because we have to create a new array of size 2N and then copy N elements over, O(2N + N) = O(3N) = O(N).
* But most of the times the `ArrayList` won't be full, and adding a new element will take O(1).

In the worst case it takes O(N), but in N-1 cases it takes O(1). Once the worst case happens, it won't happen again for so long that the cost is "amortized". If we add X elements to the `ArrayList`, it takes ~2X --> X adds take O(X) time, the amortized time for each adding is O(1).

### 1.7. Log(N) runtimes

In binary search, the number of elements in the problem space gets halved each time. Or, starting from 1, is multiplied k times until reaching N. 2<sup>k</sup>=N -> k=log<sub>2</sub>N, so O(log(N)) runtime.

### 1.8. Recursive runtimes

```c
int f(int n) {
    if(n <= 1) {
        return 1;
    }
    return f(n-1) + f(n-1);
}
```

The tree has depth of 4, and 2 branches, each node has 2 children: `f(n-1) + f(n-1)`. Each level has twice as many calls as the one above it: 2<sup>0</sup> + 2<sup>1</sup> + ... + 2<sup>N-1</sup> = 2<sup>N</sup> - 1.

When having a recursive function making multiple calls, the runtime is often (not always!) O(branches<sup>depth</sup>), where branches is the number of times each recursive call branches. In this case, the runtime is O(2<sup>N</sup>) and the space complexity O(N), because even if there are O(2<sup>N</sup>) nodes in the tree total, there are only O(N) at a given time.

### 1.9. Examples and exercises

p45 - p58.

```c
int factorial(int n) { /* example 11 */
    if (n < 0) return -1;
    if (n == 0) return 1;
    return n * factorial(n-1);
}
```

The two `if` conditions take O(1) time, otherwise it's a straight recursion from n to n-1, ..., 1. O(n) time.

```c
int fib(int n) { /* example 13 */
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fib(n-1) + fib(n-2); // 2 branches
}
```

2 branches and depth of 4, so O(2<sup>n</sup>). Being more precise, most of the nodes at the bottom of the call stack/tree, there is only one call. This single vs. double call makes a big difference, the runtime is actually closer to O(1.6<sup>n</sup>).

In general, if there are multiple recursive calls, the runtime is exponential.

```c
void allFib(int n) { /* example 14 */
    for(int i = 0; i < n; i++) {
        cout << i + ": " + fib(i) << endl;
    }
}

int fib(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fib(n-1) + fib(n-2); // 2 branches
}
```

The for loop is O(n), so multiplied by the time complexity of fib(n), which is 2<sup>n</sup>. Right? But we don't always access fib(n) with the same number, `i` is changing.

* fib(1) -> 2<sup>1</sup> steps
* fib(2) -> 2<sup>2</sup> steps
* fib(3) -> 2<sup>3</sup> steps
* fib(4) -> 2<sup>4</sup> steps
* ...
* fib(n) -> 2<sup>n</sup> steps

And we know that 2<sup>0</sup> + 2<sup>1</sup> + ... + 2<sup>N-1</sup> = 2<sup>N</sup> - 1, so our secuence 2<sup>1</sup> + ... + 2<sup>N-1</sup> = 2<sup>N</sup> - 2. So time complexity is O(2<sup>N</sup>).

What if we cache values? Also called memoization.

```c
void allFib(int n) { /* example 15 */
    int[] memo = new int[n + 1];
    for(int i = 0; i < n; i++) {
        cout << i + ": " + fib(i, memo) << endl;
    }
}

int fib(int n, int[] memo) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    if (memo[n] > 0) return memo[n];

    memo[n] = fib(n-1, memo) + fib(n-2, memo);
    return memo[n]
}
```

For each value, we look for `fib(n-1)` and `fib(n-2)`, which are already stored. We do a constant amount of work for each element, so O(n).

**Binary search tree**: a node-based binary tree data structure which has the following properties:

* The left subtree of a node contains only nodes with keys lesser than the node’s key.
* The right subtree of a node contains only nodes with keys greater than the node’s key.
* The left and right subtree each must also be a binary search tree. 

![im](https://media.geeksforgeeks.org/wp-content/uploads/BSTSearch.png){width=200}

Search in unbalanced binary search trees, or just binary trees is O(n). We might have to search through all the nodes.

## 1.2. Technical questions

### 1.2.1. How to prepare

1. Try to solve the problem on your own
2. Write the code on paper
3. Test the code on paper: general cases, base cases, error cases
4. Type the code as is into the computer

### 1.2.2. What you need to know

#### 1.2.2.1. Core data structures, algorithms and concepts

| Data structures        | Algorithms           | Concepts              |
| ---------------------- |:--------------------:| ---------------------:|
| linked lists           | breadth-first search | bit manipulation      |
| trees, tries & graphs  | depth-first search   | memory(stack vs heap) |
| stacks & queues        | binary search        | recursion             |
| heaps                  | merge sort           | dynamic programming   |
| vectors/ArrayLists     | quick sort           | big O time & space    |
| hash tables            |                      |                       |

If you don't feel comfortable with each data structure and algorithms, practice implementing them from scratch, in particular hash tables.

#### 1.2.2.2. Powers of 2 table

| Power of 2 | Approx. value | Bytes |
| ---------- |:-------------:| -----:|
| 7          |               |       |
| 8          |               |       |
| 10         | 1 thousand    | 1 KB  |
| 16         |               | 64 KB |
| 20         | 1 million     | 1 MB  |
| 30         | 1 billion     | 1 GB  |
| 32         |               | 4 GB  |
| 40         | 1 trillion    | 1 TB  |

A bit vector mapping every 32-bit integer to a boolean value, fits in memory on a typical machine. There are 2<sup>32</sup> such integers. Because each integer takes one bit in this bit vector, we need 2<sup>32</sup> bits / 2<sup>29</sup> bytes to store the mapping, about 500MB of memory.

#### 1.2.2.3. Walking through a problem

![im](https://cdn-images-1.medium.com/max/1200/1*UsPt4i_tM99tWVWa2aa29g.png)

1. Listen for unique information: sorted input arrays, an algorithm that has to be run repeatedly (-> cache data?). The optimal algorithm for these tasks depends on this information.
2. Draw an example
   1. specific to the problem: use real numbers or strings
   2. sufficiently large
   3. not a special case
3. State a brute force algorithm, even if it's terrible
   1. explain time and space complexity
   2. improve from there
4. Optimize
   1. look for unused information that the interviewer might have said, or from your input
   2. use a fresh example
   3. solve it incorrectly. solve it for some cases, not for others. and improve from there
   4. make time vs. space tradeoff
   5. precompute information: can we reorganize data (sorting, etc) or compute some values upfront that'll save time later?
   6. think about the best conceivable runtime
5. Walk through
   1. when we have an algorithm, don't code it yet. Whiteboard coding, testing and debugging is slow, we want the beginning to be as close to perfect as possible
   2. walk through the algorithm, what variables there are, when they change
6. Implement
   1. modularized code: if you have to initialize a matrix with incremental values, write `initIncrementalMatrix(int size)` and fill the details later if needed
   2. error checks: write a todo and explain out loud what you'd like to test
   3. use other classes/structs: if you have to return a list of start and end points from a function, we can use a 2D array
   4. good variable names: you can start with `startChild()`, long name, and then abbreviate and say out loud that you'll say `sc` from then on
7. Test: when finding bugs, carefully analyze them
   1. start with a conceptual test, read and analyze what each line does. Does the code do what you think it should do?
   2. double check lines that have constant numbers, `x = length - 2` or similars.
   3. hot spots: recursive code, integer division, null nodes in binary trees, start and end of interation through a linked list...
   4. small test cases: use small inputs
   5. special cases: null or single element inputs, extreme cases, or other special cases

#### 1.2.2.4. Optimize and solve technique \#1: look for BUD

BUd: bottlenecks, unnecessary work, duplicated work

* Bottleneck: part of the algorithm slowing down the overall runtime
  * one-time work that slows down runtime. if we have O(NlogN + N), it doesn't matter if we optimize the second part. the first part is the bottleneck.
  * a chunk of work done repeatedly, searching for example. maybe you can reduce it from O(N) to O(logN).
    * for example we want to search for things in an unsorted array, we can a) sort it, or b) throw everything in the array into the hash table and look it up there (O(N)). 
* Unnecessary work
  * break a loop when a solution is found
  * if we're looking for one value in an inner loop, derive it from the formula and check. 1 if condition instead of another loop
* Duplicate work
  * Use hash tables to precompute values and save runtime

#### 1.2.2.5. Optimize and solve technique \#2: do it yourself

Try working through the problem intuitively on a real eaxmple first, sometimes we have intuitive solutions to problems such as looking for words in a dictionary -> binary search in sorted array.

Or make a nice big example and **intuitively, manually, solve it for the specific example. and then check think about how you solved it.** Also consider optimizations you automatically made, like skipping some useless examples.

#### 1.2.2.6. Optimize and solve technique \#3: simplify and generalize

Implement a multi step approach:

1. simplify or tweak some constraint, such as data type
2. solve this simplified version of the problem
3. adapt the simplified case to the more complex version

#### 1.2.2.7. Optimize and solve technique \#4: base case and build

Solve the code for a base case (n=1), and then build up from there. When getting to more complex cases, try to build them using the prior solutions.

#### 1.2.2.8. Optimize and solve technique \#5: data structure brainstorm

Run through a list of data structures and try to apply each one. Consider benefits and drawbacks of each data type: sorting, indexing, searching.

#### 1.2.2.9. Best conceivable runtime

The best runtime you could ever conceive, where there is no way to beat BCR. If we have to print all pairs of values of an array, we at least have to print O(N<sup>2<sup>) values.

Start with a brute force solution, compare it with BCR, find a middle-point algorithm, for example O(logN) -> O(1). Try to think of optimizations from BUD section. Anything we do that's less or equal than BCR is 'free', it doesn't affect runtime. If we reach BCR, there's no more optimization to be done in runtime. We can focus on space complexity. In the example in p74, the algorithm with O(N) runtime also had O(N) space complexity. Improving that means O(logN) or O(1). Consider algorithms that have O(1) space, and optimize based on runtime.

If you've reached BCR and have O(1) additional space, you can't optimize big O time or space. 


## General resources

* [Cracking the coding interview solutions github](https://github.com/careercup/CtCI-6th-Edition)
* [Solutions to hackerrank problems](https://github.com/RodneyShag/HackerRank_solutions): algorithms, data structures, CtCI.
* [Leetcode](https://leetcode.com/)
* [Topcoder](https://www.topcoder.com/community/competitive-programming/tutorials/)