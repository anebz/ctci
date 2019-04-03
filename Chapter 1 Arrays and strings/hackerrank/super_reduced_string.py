# Algorithms > Strings > Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string

import unittest

def reduce_string(s):
    slen = len(s)
    if slen < 2:
        return "Empty String" if len(s) == 0 else s
    
    i = 0
    count = 0
    while slen > 1 and i < slen - 1:
        if s[i] == s[i+1]:
            count += 1
            
        if count % 2 == 1:
            s = s.replace(s[i] * (count+1), '')
            i -= count + 1
            if i < -1:
                i = -1
            slen = len(s)
            count = 0
            
        i += 1
    
    return "Empty String" if len(s) == 0 else s
    
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
