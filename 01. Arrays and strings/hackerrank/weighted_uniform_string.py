# Algorithms > Strings > Weighted Uniform Strings
# Check if the number belongs to the set of weights for all possible uniform strings in input
#
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    weights = set()
    weights.add(ord(s[0]) - 96)
    count = 1
    for i in range(1, len(s)):
        weight = ord(s[i]) - 96
        if s[i] != s[i-1]:
            count = 1
        else:
            count += 1 
        weights.add(weight * count)

    res = []
    for q in queries:
        res.append("Yes" if q in weights else "No")
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

