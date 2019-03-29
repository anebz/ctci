# Chapter 1: Arrays and strings

## 1.1. Hash tables

data structure that maps keys to values for highly efficient lookup. In this example we use an array of linked lists and a hash code function. To insert a key and value:

1. Compute the key's hash code, which will usually be an `int` or `long`. Two different keys can have the same hash code, because there can be infinite keys but there is only a finite number of integers.
2. Map the hash code to an index in the array, for example with `hash(key) % array_length`. Two different hash codes can have the same index.
3. At this index there's a liked list of keys and values, and we store the key value pair in this index. A linked list avoids collissions, you can have two different keys with the same hash code and two different hash codes mapping to the same index.

To retreat the value from a key, repeat the process. Calculate hash code, compute the index, search in the linked list.

If the number of collissions is very high, the worst case runtime is O(N), where N = \# keys. But if we implement a good system keeping collissions to a minimum, lookup is O(1).

Alternatively we can implement a lookup system with a balanced binary search tree, giving us O(logN) lookup time. It uses less space because we don't have to allocate a large array, and we can iterate through the keys in order.

## 1.2. ArrayList and resizable arrays

In some languages arrays/lists are automatically resizable, but it isn't in others such as Java. An `ArrayList` is an array that resizes itself as needed while still providing O(1) access. A typical implementation is doubling the array size when it gets full, but others increase 50% or some other number. Each resizing takes O(n) time, but happens so rarely that its amortized insertion time is still O(1).

> Why is the amortized insertion runtime O(1)
>
> Because inserting N elements, we insert 1 + 2 + N/8 + N/4 + N/2 = N (roughly). Insertin N elements takes O(N), inserting one takes O(1), even though in the worst case it'll be O(N)

## 1.3. StringBuilder

We want to concatenate a list of strings, there are `n` strings each with length `x`. 

```c
String joinWords(String[] words) {
    String sentence = "";
    for (String w : words) {
        sentence = sentence + w;
    }
    return sentence;
}
```

On each concatenation it creates a new copy of the string. It copies `x` characters, then `2x`, until `nx`. The total time is O(1x+ 2x + ... + nx) = O(xn(n+1)/2) = O(xn<sup>2</sup>).

**StringBuilder** creates a resizable array of all the strings, copying them back to a string only when necessary.

```c
String joinWords(String[] words) {
    StringBuilder sentence = new StringBuilder();
    for (String w : words) {
        sentence.append(w);
    }
    return sentence.toString();
}
```

## Resources

* [Hackerrank string exercises](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=strings)
* [Java solutions](https://github.com/careercup/CtCI-6th-Edition/tree/master/Java/Ch%2001.%20Arrays%20and%20Strings)
* [C++ solutions](https://github.com/careercup/CtCI-6th-Edition-cpp/tree/a68ba3e1c630a4d218ff1294f3eaf5aeced449ec/Ch%201.Arrays%20And%20Strings)
* [Python solutions](https://github.com/careercup/CtCI-6th-Edition-Python/tree/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter1)