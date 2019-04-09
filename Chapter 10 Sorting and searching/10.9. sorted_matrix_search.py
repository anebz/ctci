import unittest

M = 5
N = 5

def search_sorted_matrix(A, num):
    if num < A[0][0] or num > A[M-1][N-1]:
        return 0
    if num == A[0][0] or num == A[M-1][N-1]:
        return 1

    rows = [0, M-1]
    cols = [0, N-1]

    while True:
        new_rows = []
        new_cols = []
        flag = False

        if rows[0] == rows[1]:
            for j in range(cols[0], cols[1]+1):
                if A[rows[0]][j] == num:
                    return 1
            return 0

        if cols[0] == cols[1]:
            for i in range(rows[0], rows[1]+1):
                if A[i][cols[0]] == num:
                    return 1
            return 0

        # check bounded rows
        for i in range(rows[0], rows[1]+1):
            if A[i][cols[0]] == num or A[i][cols[1]] == num:
                return 1
            if A[i][cols[0]] > num:
                new_rows.append(i - 1)
                flag = False
                break
            if i == rows[1]:
                new_rows.append(i)
                flag = False
                break
            if A[i][cols[0]] < num and A[i][cols[1]] > num:
                if not flag:
                    new_rows.append(i)
                    flag = True

        # check bounded cols
        for j in range(cols[0], cols[1]+1):
            if A[rows[0]][j] == num or A[rows[1]][j] == num:
                return 1
            if A[rows[0]][j] > num:
                new_cols.append(j - 1)
                flag = False
                break
            if j == cols[1]:
                new_cols.append(j)
                flag = False
                break
            if A[rows[0]][j] < num and A[rows[1]][j] > num:
                if not flag:
                    new_cols.append(j)
                    flag = True

        if len(new_rows) == len(new_cols) == 1 or new_rows[0] == new_rows[1] and new_cols[0] == new_cols[1]:
            return 0

        rows = new_rows
        cols = new_cols

    return 0

class Test(unittest.TestCase):
    data = [
        ([
            [0, 1, 3, 4, 6],
            [1, 3, 4, 7, 14],
            [3, 12, 13, 14, 15],
            [6, 17, 18, 25, 26],
            [8, 22, 23, 28, 30]
        ], 2, 0)
    ]

    def test_rotate_matrix(self):
        for test_matrix, num, expected in self.data:
            actual = search_sorted_matrix(test_matrix, num)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
