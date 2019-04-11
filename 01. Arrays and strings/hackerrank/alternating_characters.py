# Algorithms > Strings > Alternating Characters 
# https://www.hackerrank.com/challenges/alternating-characters

import unittest

def alternatingCharacters(s):
    if len(set(s)) == 1:
        return len(s) - 1

    res = len(s) - max(s.count("AB"), s.count("BA"))*2
    if s[0] == s[-1]:
        res -= 1
    return res

class Test(unittest.TestCase):

    data = [('AAAA', 3),
            ('BBBBB', 4),
            ('ABABABAB', 0),
            ('BABABA', 0),
            ('AAABBB', 4),
            ('ABABABAA', 1)]


    def test(self):
        for test_string, expected in self.data:
            res = alternatingCharacters(test_string)
            self.assertEqual(res, expected)

if __name__ == "__main__":
    unittest.main()
