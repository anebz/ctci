# Algorithms > Strings > Strong Password
# https://www.hackerrank.com/challenges/strong-password

import unittest

def minimumNumber(s):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    count = 0
    if not any(x in numbers for x in s):
        count += 1
    if not any(x in lower_case for x in s):
        count += 1
    if not any(x in upper_case for x in s):
        count += 1
    if not any(x in special_characters for x in s):
        count += 1
    
    return max(count, 6-len(s))

class Test(unittest.TestCase):

    data = [('Ab1', 3),
            ('#HackerRank', 1)]

    def test(self):
        for test_string, expected in self.data:
            res = minimumNumber(test_string)
            self.assertEqual(res, expected)

if __name__ == "__main__":
    unittest.main()
