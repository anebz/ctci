# Chapter 8 Recursion and dynamic programming

You can know a problem is recursive when it can be built off of subproblems. If a program says: compute the nth, or the first n, or all..., it might be recursive.

## How to approach

* Bottom-up approach: solve the problem for a simple case, then for 2 elements, then 3, etc.
* Top-down approach: think about how to divide the problem for case N into subproblems
* Half-and-half approaches: divide the dataset in half, for example binary search, merge sort.

## Recursive vs. iterative solutions

Recursive algorithms are very space inefficient, each recursive call adds a new layer to the stack. If your algorithm recurses to a depth of n, it uses at least O(n) memory.

It's better to implement a recursive algorithm iteratively. All recursive algorithms can be implemented this way, but sometimes its complex. Think how easy it would be, and discuss the tradeoffs with the interviewer.

## Dynamic programming and memoization

Dynamic programming is mostly just a matter of taking a recursive algorithm and finding the overlapping subproblems (that is, the repeated calls). You then cache those results for future recursive calls.

> Fibonacci numbers

```cpp
int fibonacci(int i) {
    if (i == 0) return 0;
    if (i == 1) return 1;
    return fibonacci(i-1) + fibonacci(i-2);
}
```

Since the calls are branched out like in a tree, each node has 2 children, each children has 2 children, the runtime is roughlt O(2<sup>n</sup>).

### Top-down, or memoization

Each time we compute fib(i), we should just cache this result and use it later.

```cpp
int fibonacci(int n) {
    return fibonacci(n, new int[n+1]);
}

int fibonacci(int i, int[] memo) {
    if (i == 0 || i == 1) return i;
    if (memo[i] == 0) {
        memo[i] = fibonacci(i-1, memo) + fibonacci(i-2, memo);
    }
    return memo[i];
}
```

The runtime now is O(n).

### Bottom-up

```cpp
int fibonacci(int n) {
    if (i == 0 || i == 1) return i;

    int[] memo = new int[n+1];
    memo[0] = 0;
    memo[1] = 1;
    for(int i = 2; i <= n; i++) {
        memo[i] = memo[i-1] + memo[i-2];
    }
    return memo[n]
}
```

But memo[i] are only used for memo[i+1], memo[i+2]. After that they're not used. We can get rid of the memo table and just store a few variables.

```cpp
int fibonacci(int n) {
    if (i == 0) return 0;

    int a = 0;
    int b = 1;
    for(int i = 2; i <= n; i++) {
        int c = a + b;
        a = b;
        b = c;
    }
    return c;
}
```
