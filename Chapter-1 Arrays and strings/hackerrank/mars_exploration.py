# Algorithms > Strings > Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration

import unittest
import numpy as np

''' O(n), O(n)
def difference(s):
    inputs = 'SOS' * int(len(s)/3)

    if s is inputs:
        return 0

    count = 0
    for a, b in zip(inputs, s):
        if a != b:
            count += 1

    return count
'''

# O(n/3), O(1)
def difference(s):
    count = 0
    for i in range(0, len(s), 3):
        if s[i] != 'S':
            count += 1
        if s[i+1] != 'O':
            count += 1
        if s[i+2] != 'S':
            count += 1
    return count

class Test(unittest.TestCase):

    data = [('SOS', 0),
            ('SOA', 1),
            ('SOSSASSEDAAA', 6)]

    def test(self):
        for test_string in self.data:
            res = difference(test_string[0])
            self.assertEqual(res, test_string[1])

if __name__ == "__main__":
    unittest.main()
