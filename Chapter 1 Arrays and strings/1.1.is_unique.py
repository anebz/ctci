# O(N)
import unittest

def is_unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

# don't understand this
def is_unique_checker(string):
    checker = 0
    for char in string:
        val = ord(char) - ord('a')
        if (checker and (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            res = is_unique(test_string)
            self.assertTrue(res)
        # false check
        for test_string in self.dataF:
            res = is_unique(test_string)
            self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()
