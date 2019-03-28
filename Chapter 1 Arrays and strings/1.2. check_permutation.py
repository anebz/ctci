import unittest

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
        if checker[ascii_val] == 0:
            del checker[ascii_val]
        if checker[ascii_val] < 0:
            return False
    if checker == {}:
        return True
    else:
        return False

class Test(unittest.TestCase):
    dataT = [('abcd', 'dbca'), ('dfgh', 'dfgh'), ('', '')]
    dataF = [('aane', 'anee'), ('ab', 'ca'), ('ane', 'aane')]

    def test(self):
        # true check
        for test_string in self.dataT:
            s1, s2 = test_string
            res = check_permutation(s1, s2)
            self.assertTrue(res)
        # false check
        for test_string in self.dataF:
            s1, s2 = test_string
            res = check_permutation(s1, s2)
            self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()
