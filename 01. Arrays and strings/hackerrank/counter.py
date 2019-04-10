# Python > Collections > collections.Counter()
# Use a counter to sum the amount of money earned by the shoe shop owner.
#
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

def calc_shoes():
    input() # no. of shoes not used
    shoes = Counter(input().split())

    money = 0
    for _ in range(int(input())):
        shoe, price = input().split()
        if shoe in shoes:
            shoes[shoe] -= 1
            if shoes[shoe] >= 0:
                money += int(price)

    return money

if __name__ == "__main__":
    print(calc_shoes())
