import unittest

inttochar = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

inttodec = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    3: "thir",
    4: "for",
    5: "fif"
}

inttoext = {
    1: "teen",
    0: "ty"
}

def inttostrings(num, numlst):

    ret = ""
    if numlst[0] == 1:
        if num in inttodec:
            return inttodec[num]
        if numlst[1] in inttodec:
            return inttodec[numlst[1]] + inttoext[1]
        else:
            return inttochar[numlst[1]] + inttoext[1]
    if numlst[0] in inttodec:
        if numlst[0] != 0:
            ret += inttodec[numlst[0]] + inttoext[0] + " "
        return ret + inttochar[numlst[1]]
    if numlst[0] != 0:
            ret += inttochar[numlst[0]] + inttoext[0] + " "
    return ret + inttochar[numlst[1]]

def int_to_eng(num):

    if num < 0:
        return -1
    if num == 0:
        return "zero"
    if num < 10:
        return inttochar[num]
    
    res = ""
    numlst = list(map(int, str(num)))

    for i in range(len(numlst)-1):
        numlst[-2-i] = inttostrings(num, numlst[-2-i:])
        numlst.pop(-1)

    return "".join(numlst)


class Test(unittest.TestCase):
    data = [(12, "twelve"),
            (16, "sixteen"),
            (45, "forty five"),
            (33, "thirty three")]

    def test_rotate_matrix(self):
        for test_num, expected in self.data:
            actual = int_to_eng(test_num)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
