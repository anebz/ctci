import unittest

dct = ['a', 'i', 'am', 'not', 'he', 'the', 'they', 'my', 
      'alive', 'darkness', 'friend', 'hello']

def re_space(s):

    s = s.lower()
    if s in dct:
        return s

    ins = s
    keywords = []
    n = len(ins)
    for i in range(n-1, 0, -1):
        j = 0
        while j + i <= n:
            tmp = ins[j:j+i]
            if tmp in dct:
                keywords.append(tmp)
                ins = ins.replace(tmp, '')
            j += 1
        n = len(ins)

    keywords = sorted(keywords)
    touched = [0] * len(s)
    for keyw in keywords:
        idx = s.find(keyw)
        if touched[idx] == 1:
            continue
        touched[idx:idx + len(keyw) + 1] = [1] * len(keyw)
        s = s.replace(keyw, ' ' + keyw + ' ')
    s = s.replace('  ', ' ')

    if s[-1] == ' ':
        s = s[:-1]
    if s[0] == ' ':
        s = s[1:]
    return s

class Test(unittest.TestCase):
    data = [('iamalive', 'i am alive'),
            ('hellodarknessmyfriend', 'hello darkness my friend'),
            ('invincibleami', 'i nv i nc i ble am i')]

    def test_rotate_matrix(self):
        for test_num, expected in self.data:
            actual = re_space(test_num)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
