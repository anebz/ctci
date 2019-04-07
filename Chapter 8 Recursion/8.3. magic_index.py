import unittest

def magic_index(s):
    if not s:
        return -1
    if s[0] == 0:
        return 0
    idx1 = 0
    idx2 = 0
    nonvisited = [i for i in range(len(s))]
    while len(nonvisited) > 1:
        if s[idx1] == idx1:
            return idx1

        idx2 = s.index(idx2)
        s[idx2] = 0
        nonvisited.remove(idx2)

        if idx1 == idx2:
            return nonvisited[0]

        val = s[idx1]
        s[idx1] = 0
        nonvisited.remove(idx1)
        idx1 = val

        if idx1 == idx2:
            return nonvisited[0]

    return -1

class Test(unittest.TestCase):

    data = [([], -1),
            ([2,1,0], 1),
            ([1,2,0], -1),
            ([1,2,3,4,0,5], 5),
            ([7,4,5,3,2,0,6,1], 3),]

    def test_unique(self):
        for test in self.data:
            res = magic_index(test[0])
            self.assertEqual(res, test[1])
        return

if __name__ == "__main__":
    unittest.main()
