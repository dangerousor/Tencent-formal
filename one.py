#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

if __name__ == '__main__':
    n, m = sys.stdin.readline().split()
    n = int(n)
    m = int(m)
    res = (n / (2 * m)) * m * m
    print(int(res))
