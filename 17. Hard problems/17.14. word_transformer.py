import unittest

dct = ["damp", "lamp", "limp", "lime", "like"]

def transform(s1, s2):

    if len(s1) != len(s2):
        return -1

    n = len(s1)
    found = [0] * n
    steps = 0
    for i in range(n):
        pos_s = s1[:i] + s2[i] + s1[i+1:]
        if pos_s in dct and not found[i]:
            s1 = pos_s
            found[i] = 1
            steps += 1

    for i in range(n):
        if found[i]:
            continue
        pos_s = s1[:i] + s2[i] + s1[i+1:]
        if pos_s in dct:
            s1 = pos_s
            found[i] = 1
            steps += 1

    return steps

class Test(unittest.TestCase):
    data = [(('damp', 'like'), 4)]

    def test_rotate_matrix(self):
        for test_num, expected in self.data:
            actual = transform(*test_num)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
