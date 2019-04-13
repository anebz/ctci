# Algorithms > Strings > Making Anagrams
# https://www.hackerrank.com/challenges/making-anagrams

import unittest
from collections import Counter

def makingAnagrams(s1, s2):
    counts = Counter(s1)
    counts.subtract(s2)
    return sum(abs(x) for x in counts.values())

class Test(unittest.TestCase):

    data = [(('a', 'b'), 2),
            (('ab', 'ab'), 0),
            (('abc', 'amnop'), 6),
            (('cde', 'abc'), 4),
            (('cde', 'abcc'), 5)]

    def test(self):
        for test_string, expected in self.data:
            res = makingAnagrams(*test_string)
            self.assertEqual(res, expected)

if __name__ == "__main__":
    unittest.main()
