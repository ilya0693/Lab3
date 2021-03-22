#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    m = int(input("Введите число m: "))

    if m == 1:
        print("Понедельник")
    elif m == 2:
        print("Вторник")
    elif m == 3:
        print("Среда")
    elif m == 4:
        print("Четверг")
    elif m == 5:
        print("Пятница")
    elif m == 6:
        print("Суббота")
    elif m == 7:
        print("Воскресенье")
    else:
        print("Ошибка!", file=sys.stderr)
        exit(1)
