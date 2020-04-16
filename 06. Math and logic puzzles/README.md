# Chapter 6. Math and logic puzzles

## 6.1. Prime numbers

Every positive integer can be decomposed into a product of primes.

If y can be divided by x, written like x\y, then all primes in x's prime factorization must be in y's prime factorization.

### 6.1.1. Checking for primality

```cpp
boolean primeNaive(int n){
    if(n < 2){
        return false;
    }
    for (int i = 2; i < n; i++) {
        if (n % i == 0){
            return false;
        }
    }
    return true;
}

boolean primeSlightlyBetter(int n){
    if (n< 2) {
        return false;
    }
    int sqrt = (int) Math.sqrt(n);
    for (int i = 2; i <= sqrt; i++) {
        if (n % i == 0) return false;
    }
    return true;
}
```

`n` not being prime means that n=a * b, for a number of a,b different than 1 and n.

* a = b, n is directly not prime
* a < b
* a > b

Either both numbers are the same, or there's a 'big' number and a 'small' number. Always. Because the multiplicators center around the square root. For a fixed number, if you make one multiplicator higher, you have to make the other smaller.

Therefore searching for the smaller number is enough. If we don't find any 'small' number divisor, then **the number must be prime**. Because if it had 2 divisors greater than sqrt, then the multiplication of those 2 numbers would be > n.

Other optimizations include iterating only over prime numbers, dynamic programming.

### 6.1.2. The sieve of Eratosthenes

Generates a list of primes taking the advantage that all non-prime numbers are divisible by a prime number.

```cpp
void std::vector<bool> sieveOfEratosthenes(int max) {
    std::vector<bool> flags(max + 1);

    init(flags); // set all flags to true other than 0 and 1.
    int prime = 2;

    while (prime <= sqrt(max)) {
        crossOff(flags, prime);
        prime = getNextPrime(flags, prime);
    }
    return flags;
}

void crossOff(boolean[] flags, int prime) {
    /* Cross off remaining multiples of prime. We can start with prime*prime), because if we have a k * prime, where k < prime, this value would have already been crossed off in a prior iteration, namely in the iteration of k.
    if prime=5, we can start at 25 because 5*2=10, 5*3=15, 5*4=20 are already crossed off.*/
    for (int i = prime * prime; i < flags.length; i += prime) {
        flags[i] = false;
    }
}

int getNextPrime(boolean[] flags, int prime) {
    int next = prime + 1;
    // find next number in flags which is True
    while (next < flags.length && !flags[next]) {
        next++;
    }
    return next;
}
```

## 6.2. Probability

* Bayes' Theorem: P(AB) = P(B|A) * P(A) = P(A|B) * P(B)
* P(A+B) = P(A) + P(B) - P(AB).
* If two events are independent, P(AB) = P(A) * P(B)
* If two events are mutually exclusive, P(A+B) = P(A) + P(B)

## 6.3. Start talking

Write the problem down. Many brainteasers are worst-case minimization problems, in terms of minimizing an action or in doing something at most a specific number of times.

A useful technique is to try to "balance" the worst case. That is, if an early decision results in a skewing of the worst case, we can sometimes change the decision to balance out the worst case.
