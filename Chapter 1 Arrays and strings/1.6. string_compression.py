import unittest

def string_compression(s):
    compr = []
    count = 0

    for i in range(len(s)):
        if i != 0 and s[i] != s[i - 1]:
            compr.append(s[i - 1] + str(count))
            count = 0
        count += 1

    compr.append(s[-1] + str(count))
    return min(s, ''.join(compr), key=len)

class Test(unittest.TestCase):

    data = [("" , ""),
            ("a", "a"),
            ("aa", "aa"),
            ("aabbb", "a2b3"),
            ("aabbbc", "aabbbc")]

    def test_unique(self):
        for test in self.data:
            res = compress(test[0])
            self.assertEqual(res, test[1])
        return

if __name__ == "__main__":
    unittest.main()
