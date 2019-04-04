# Algorithms > Strings > Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string

import unittest

def reduce_string(s):
    slen = len(s)
    if slen < 2:
        return s if s else "Empty String"
    
    i = 0
    count = False
    while slen > 1 and i < slen - 1:
        if s[i] == s[i+1]:
            count = True
            
        if count:
            s = s.replace(s[i] * 2, '')
            i = max(i-2, -1)
            slen = len(s)
            count = False
            
        i += 1
    
    return s if s else "Empty String"
    
class Test(unittest.TestCase):
    
    data = [('', "Empty String"),
            ('aaabbb', 'ab'),
            ('aabb', "Empty String"),
            ('aadbbc', 'dc'),
            ('abcdeedcba', "Empty String"),
            ('abcdeeedcba', 'abcdedcba'),
            ('aabbbcaacbd', 'd'),
            ('ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeeyyaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx', 'Empty String')]
    
    def test(self):
        for test_string in self.data:
            res = reduce_string(test_string[0])
            self.assertEqual(res, test_string[1])

if __name__ == "__main__":
    unittest.main()
