import unittest

def pal_perm(s):
    s = s.lower()

    if len(s) <= 1:
        return True
    if len(s) == 2:
        return s[0] == s[1]

    freq = {}
    flag = 0
    for char in s:
        # if not a letter
        if ord(char) not in range(65, 91) and ord(char) not in range(97, 123):
            s.replace(char, '')
            
        if char not in freq:
            freq[char] = 1
            flag += 1
        else:
            freq[char] += 1
            if freq[char] % 2 == 0:
                flag -= 1
            else:
                flag += 1
    return flag <= 1


class Test(unittest.TestCase):
    dataT = ['', 'a', 'aa', 'asddsa', 'asdfdsa', 'asdadsa', 'aaaaa', 'aaaa']
    dataF = ['as', 'ane', 'adsa', 'assdadsa']

    def test_unique(self):
        for test in self.dataT:
            res = pal_perm(test)
            self.assertTrue(res)

        for test in self.dataF:
            res = pal_perm(test)
            self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()
