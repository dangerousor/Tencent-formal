#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

if __name__ == '__main__':
    n, m = sys.stdin.readline().split()
    n = int(n)
    m = int(m)
    machine = []
    task = []
    for i in range(n):
        x, y = sys.stdin.readline().split()
        machine.append([int(x), int(y), False])
    for i in range(m):
        x, y = sys.stdin.readline().split()
        task.append([int(x) * 200 + int(y) * 3, int(x), int(y)])
    resn = 0
    resv = 0
    task = sorted(task)
    for each in task:
        for every in machine:
            if not every[2] and every[0] >= each[1] and every[1] >= each[2]:
                resn = resn + 1
                resv = resv + each[0]
                every[2] = True
                break
    print(resn, resv)
