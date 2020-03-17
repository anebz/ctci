# Chapter 5. Bit manipulation

page 127. hints start at 673

## 5.1. Two's complement and negative numbers

Positive numbers are represented as themselves, negative numbers as the two's complement of its absolute value, with a 1 in its sign bit, indicating it's negative.

The two's complement of an N-bit number (N: \# bits used for the number, excluding the sign bit), is the complement of the number with respect to 2<sup>N</sup>.

The binary representation of -K as a N-bit number is concat(1, 2<sup>N-1</sup> - K).

## 5.2. Arithmetic vs. Logical right shift

Arithmetic right shift: division by two. Logical right shift: 'shifting the bits'.

### 5.2.1. Logical shift

Indicated with a >>> operator, all bits are shifted, sign bit too.

* -75: **1**0110101
* 90: **0**1011010

```c++
int repeatedLogicalShift(int x, int count) {
    for (int i = 0; i < count; i++) {
        x >>>= 1; // Logical shift by 1
    }
}
```

### 5.2.2. Arithmetic shift

The sign bit is kept, and all bits (sign bit too) are shifted.

* -75: **1**0110101
* -38: **1**1011010

```c++
int repeatedArithmeticShift(int x, int count) {
    for (int i = 0; i < count; i++) {
        x >>= 1; // Arithmetic shift by 1
    }
}
```

## 5.3. Common bit tasks: getting and setting

### Get bit

This method shifts 1 over by i bits, creating a value that looks like 00010000. By performing an AND with `num`, we clear all bits other than the bit at bit `i`. Then we compare it to 0. If the new value isn't 0, then bit i must have a 1. Otherwise, bit i is a 0.

```c++
boolean getBit(int num, int i) {
    return ((num & (1 << i)) != 0);
}
```

### Set bit

This function shifts 1 over by i bits, creating a value like 00010000. By performing an OR with `num`, only the value at bit i will change. All other bits of the mask are zero, and won't affect `num`. It sets the bit to 1 if it's 0, otherwise leaves the number unchanged.

```c++
boolean setBit(int num, int i) {
    return num | (1 << i);
}
```

### Clear bit

This is the opposite of `setBit`. We first create a number like 11101111. Then, we AND it with `num`. This clears the bit i and leaves the rest unchanged.

```c++
boolean clearBit(int num, int i) {
    return num & ~(1 << i);
}
```

To clear all bits from the most significant bit through i (inclusive), we create a mask with a 1 at the ith bit (1 << i). Then we substract 1 from it, giving us a sequence of zeros followed by i ones. We AND `num` with this mask, to leave just the last i bits.

```c++
boolean clearBitMSBthroughI(int num, int i) {
    return num & ((1 << i) - 1);
}
```

To clear all bits from i through 0 (inclusive), we take a sequence of all ones (which represents -1) and shift it left by i+1 bits. This gives a sequence of ones followed by i+1 zeros.

```c++
boolean clearBitIthrough0(int num, int i) {
    return num & (-1 << (i+1));
}
```

### Update bit

To set the ith bit to a value v, we first clear the bit at position i, then we shift the value v, left by i bits. This will create a number with bit i equal to v and all other bits equal to 0. Finally, we OR these 2 numbers, updating the ith bit if v=1 and leaving it as 0 otherwise.

```c++
boolean updateBit(int num, int i, boolean bitIs1) {
    int value = bitIs1 ? 1 : 0;
    int mask = ~(1 << i);
    return (num & mask) | (value << i);
}
```
