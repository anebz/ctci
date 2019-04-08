import unittest

M = 5 - 1
N = 5 - 1

def search_sorted_matrix(A, num):
    if num < A[0][0] or num > A[M][N]:
        return 0
    if num == A[0][0] or num == A[M][N]:
        return 1
    if num < A[0][N]:
        initidx = 0
        maxidx = N
        while True:
            i = maxidx // 2
            if A[0][i] == num:
                return 1
            elif A[0][i] > num:
                maxidx = i
            elif A[0][i] < num:
                initidx = i

            if A[0][initidx] < num and A[0][initidx+1] > num:
                break
    return 0

class Test(unittest.TestCase):
    data = [
        ([
            [0, 1, 3, 4, 6],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], 2, 1)
    ]

    def test_rotate_matrix(self):
        for test_matrix, num, expected in self.data:
            actual = search_sorted_matrix(test_matrix, num)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
