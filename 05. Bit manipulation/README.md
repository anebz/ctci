# Chapter 5. Bit manipulation

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

### 5.2.2. Arithmetic shift

The sign bit is kept, and all bits (sign bit too) are shifted.

* -75: **1**0110101
* -38: **1**1011010

## 5.3. Common bit tasks: getting and setting