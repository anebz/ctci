# Algorithms > Strings > Anagram
# https://www.hackerrank.com/challenges/anagram

import unittest
from collections import Counter

def anagram(s):
    if len(s) % 2 == 1:
        return -1
    counts = Counter(s[:len(s)//2])
    counts.subtract(s[len(s)//2:])
    return sum(abs(x) for x in counts.values())//2

class Test(unittest.TestCase):

    data = [('aaabbb', 3),
            ('ab', 1),
            ('abc', -1),
            ('mnop', 2),
            ('xyyx', 0),
            ('xaxbbbxx', 1)]

    def test(self):
        for test_string, expected in self.data:
            res = anagram(test_string)
            self.assertEqual(res, expected)

if __name__ == "__main__":
    unittest.main()
