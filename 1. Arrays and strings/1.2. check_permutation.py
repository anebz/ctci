import unittest
from time import time
from collections import Counter

def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    checker = dict()
    for char in s1:
        ascii_val = ord(char)
        if ascii_val not in checker:
            checker[ascii_val] = 1
        else:
            checker[ascii_val] += 1

    for char in s2:
        ascii_val = ord(char)
        if ascii_val not in checker:
            return False
        checker[ascii_val] -= 1
        if checker[ascii_val] < 0:
            return False
    return True

def check_permutation_pythonic(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) <= 1:
        return True

    counter = Counter()
    for char in s1:
        counter[char] += 1
    for char in s2:
        if counter[char] == 0:
            return False
        counter[char] -= 1
    return True

class Test(unittest.TestCase):
    dataT = [('abcd', 'dbca'), ('dfgh', 'dhgf'), ('', '')]
    dataF = [('aane', 'anee'), ('ab', 'ca'), ('ane', 'aane')]

    def test(self):
        # true check
        for test_string in self.dataT:
            start = time()
            res = check_permutation(*test_string)
            self.assertTrue(res)
            print(f"{time() - start}s")

            start = time()
            res = check_permutation_pythonic(*test_string)
            self.assertTrue(res)
            print(f"{time() - start}s")

        # false check
        for test_string in self.dataF:
            start = time()
            res = check_permutation(*test_string)
            self.assertFalse(res)
            print(f"{time() - start}s")

            start = time()
            res = check_permutation_pythonic(*test_string)
            print(f"{time() - start}s")
            self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()
