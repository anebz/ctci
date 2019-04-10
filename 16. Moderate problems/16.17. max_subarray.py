import unittest

def cont_seq(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(max(nums), sum(nums))
    if max(nums) < 0:
        return max(nums)
    if max(nums) == min(nums):
        return max(nums)

    maxval = 0
    count = 0
    for n in nums:
        count += n
        if count  < 0:
            count = 0
        elif count > maxval:
            maxval = count

    return maxval

class Test(unittest.TestCase):
    data = [([], 0),
            ([2, -8, 3, -2, 4, -10], 5),
            ([2, -12, 3, -5, 4, -10], 4),
            ([2, 1, 1, 1, -8, 3, -1, 4, -2, 3, -1, -1, -1, -3, -6], 7),
            ([3, -1, 4, -2, 3, -1, -1, 3, -3, -6], 8),
            ([3, -1, 4, -2, 3, -1, -3, 3, -6, 4], 7),
            ([4, -3, 3, -4, 4, -1, 1, 3, -7], 7),
            ([4, -3, 3, -4, 4, -1, 1, 3, -7, 2, 2, 4], 8)]

    def test_rotate_matrix(self):
        for nums, expected in self.data:
            res = cont_seq(nums)
            self.assertEqual(res, expected)

if __name__ == "__main__":
    unittest.main()
