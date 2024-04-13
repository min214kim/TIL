orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

from itertools import combinations as com

for n in course:
    combinations = []
    for order in orders:
        o = list(order)
        c = list(com(o, n))
        combinations += c
        for r in range(len(combinations)):
            