#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    for i in range(105, 701, 7):
        d, u = i // 10, i % 10
        h, d = d // 10, d % 10
        if h + d + u == 7:
            print(i)