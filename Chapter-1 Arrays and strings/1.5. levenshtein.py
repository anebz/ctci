import unittest

def levenshtein(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    if s1 == s2:
        return True
    
    len1 = len(s1)
    len2 = len(s2)
    flag = False

    if len1 == len2:  # equal lengths
        for i in range(len1):
            if s1[i] != s2[i]:
                if flag:
                    return False
                flag = True
        return True
    
    elif len1 < len2:  # s1 shorter than s2
        for i in range(len1):
            if not flag:
                if s1[i] != s2[i]:
                    if flag:
                        return False
                    flag = True
            else: # there's already one difference
                if s1[i] != s2[i + 1]:
                    return False
        return True

    elif len2 < len1:  # s2 shorter than s1
        for i in range(len2):
            if not flag:
                if s1[i] != s2[i]:
                    if flag:
                        return False
                    flag = True
            else:  # there's already one difference
                if s1[i + 1] != s2[i]:
                    return False
        return True

class Test(unittest.TestCase):
    dataT = [("", ""), ("an", "a"), ("a", "an"), ("ane", "ae"),
             ("ane", "ne"), ("asdfgh", "asdgh"), ("asdf", "asgf")]
    dataF = [("asdfg", "adfgh"), ("an", "ne"), ("asdf", "as")]

    def test_unique(self):
        for test in self.dataT:
            res = levenshtein(*test)
            self.assertTrue(res)

        for test in self.dataF:
            res = levenshtein(*test)
            self.assertFalse(res)

        return

if __name__ == "__main__":
    unittest.main()
