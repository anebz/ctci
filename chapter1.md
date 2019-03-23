# Chapter 1

## Big O

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

* Add runtime: do A chinks of work, then B chunks of work

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