#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


def stepplus(n):
    if n == 0:
        return 1
    r = 1
    for t in range(1, n + 1):
        r = r * t
    return r


def collect(n, m):
    t_x = stepplus(n) / (stepplus(n - m) * stepplus(m))
    print("step %d, %d:\t" % (n, m), t_x)
    return t_x


if __name__ == '__main__':
    k = int(sys.stdin.readline().strip())
    temp = sys.stdin.readline().split()
    a, x, b, y = [int(each) for each in temp]
    # k = 1
    # a, x, b, y = [1, 100, 10, 100]
    res = 0
    temp_y = y
    for i in range(x + 1):
        if a * i > k:
            break
        for j in range(temp_y + 1):
            if i * a + (temp_y - j) * b == k:
                print(i, temp_y-j)
                res = res + collect(x, i) * collect(y, (temp_y - j))
                temp_y = temp_y - j
                break
            if i * a + (temp_y - j) * b < k:
                temp_y = temp_y - j
                break
    print(divmod(int(res), 1000000007)[1])
    print(collect(100, 50))
    print(collect(100, 50) == collect(99, 50) + collect(99, 49))

