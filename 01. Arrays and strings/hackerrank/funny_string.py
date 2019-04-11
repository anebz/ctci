# Algorithms > Strings > Funny string
# https://www.hackerrank.com/challenges/funny-string/

import unittest

def funnyString(s):
    if len(s) < 2:
        return "Funny"
    
    for i in range(1,len(s)//2):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[-i]) - ord(s[-i-1])):
            return "Not Funny"

    return "Funny"

class Test(unittest.TestCase):

    data = [('acxz', 'Funny'),
            ('bcxz', 'Not Funny'),
            ('bcccd', 'Funny')]

    def test(self):
        for test_string, expected in self.data:
            res = funnyString(test_string)
            self.assertEqual(res, expected)

if __name__ == "__main__":
    unittest.main()
