# Algorithms > Strings > The Love-Letter Mystery
# https://www.hackerrank.com/challenges/the-love-letter-mystery

import unittest

def theLoveLetterMystery(s):
    
    if len(s) == 1:
        return 0
    
    count = 0
    for i in range(len(s)//2):
        count += abs(ord(s[i]) - ord(s[-1-i]))

    return count

class Test(unittest.TestCase):

    data = [('abc', 2),
            ('abcba', 0),
            ('abcd', 4),
            ('cba', 2)]


    def test(self):
        for test_string, expected in self.data:
            res = theLoveLetterMystery(test_string)
            self.assertEqual(res, expected)

if __name__ == "__main__":
    unittest.main()
