import unittest

def replace_char(s, maxlen):
    maxlen = max(0, maxlen)
    maxlen = min(maxlen, len(s))
    new_s = ''
    for i in range(maxlen):
        if s[i] == ' ':
            new_s += '%20'
        else:
            new_s += s[i]
    return new_s

class Test(unittest.TestCase):
    data = [(('', 3), ''),
            (('  ', 3), '%20%20'),
            (('ane  ', 3), 'ane'), 
            (('ane  ', 4), 'ane%20'),
            (('a ne  ', 8), 'a%20ne%20%20')]

    def test(self):
        for test_string in self.data:
            res = replace_char(*(test_string[0]))
            self.assertEqual(res, test_string[1])

if __name__ == "__main__":
    unittest.main()
