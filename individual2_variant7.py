#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


if __name__ == '__main__':
    print('Решим биквадратное уравнение a*x**4 + b*x**2 + c = 0')
    a = float(input("Value of a? "))
    b = float(input("Value of b? "))
    c = float(input("Value of c? "))
    if a == 0:
        print("Illegal value of a", file=sys.stderr)
        exit(1)

    print("Решим квадратное уравнение ay**2 + by + c = 0")

    print("1. Вычислим дискриминант:")
    D = b ** 2 - 4 * a * c
    print(f"D = {D}")

    print("2. Найдем корни y")
    if D < 0:
        print("Корней нет")
        exit(1)
    elif D == 0:
        y = -b / (2 * a)
        print(f"y = {y}")
    else:
        y1 = (-b + math.sqrt(D)) / (2 * a)
        y2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"y1 = {y1}")
        print(f"y2 = {y2}")

    print("3. Решим уравнение x")
    z1 = y1
    z2 = y2

    x1 = math.sqrt(z1)
    x2 = - math.sqrt(z1)
    x3 = math.sqrt(z2)
    x4 = - math.sqrt(z2)

print(f"x1 = {x1}\nx2 = {x2}\nx3 = {x3}\nx4 = {x4}")