import unittest
from collections import Counter

def rotate_matrix(s1, s2):

    if len(s1) != len(s2) or Counter(s1) != Counter(s2):
        return 0
    if len(s1) < 3 or s1 == s2:
        return 1

    indexes = [i for i, e in enumerate(s2) if e == s1[0]]
    for idx in indexes:
        offset = len(s1) - idx
        if s2[idx:] == s1[:offset] and s2[:idx] == s1[offset:]:
            return 1
    return 0


class Test(unittest.TestCase):
    '''Test Cases'''
    dataT = [('', ''),
             ('a', 'a'),
             ('ab', 'ba'),
             ('waterbottle', 'waterbottle'),
             ('erbottlewat', 'waterbottle'),
             ('qwerqwer', 'erqwerqw')]

    dataF = [('', 'a'),
            ('a', 'b'),
            ('qwerq', 'wreqq')]

    def test_rotate_matrix(self):
        for test in self.dataT:
            res = rotate_matrix(*test)
            self.assertTrue(res)

        for test in self.dataF:
            res = rotate_matrix(*test)
            self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()