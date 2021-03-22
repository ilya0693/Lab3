#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


if __name__ == '__main__':
    for i in range(105, 701, 7):
        d, u = divmod(i, 10)
        h, d = divmod(d, 10)
        if h + d + u == 7:
            print(i)