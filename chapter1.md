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