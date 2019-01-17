# �������� ���������, ������������ ��� �����������, ��� ��� ��������� ����������� ����� 
# ����������� ���������: 1+2+...+n = n(n+1)/2, ��� n - ����� ����������� �����.

import cProfile
import functools
import timeit

# 1. Loop

def summ_numbers_loop(n):
    i = 0
    summ = 0

    while i < n:
        i = i + 1
        summ = summ + i
    return summ


cProfile.run('summ_numbers_loop(1000000)')
#print(timeit.Timer(summ_numbers_loop(10)).timeit(number=100))

#1    0.402    0.402    0.402    0.402 4_1.py:8(summ_numbers_loop) - 1 000 000
#1    3.670    3.670    3.670    3.670 4_1.py:8(summ_numbers_loop) - 10 000 000
#1   28.527   28.527   28.527   28.527 4_1.py:8(summ_numbers_loop) - 100 000 000
# ���� ������������ ��������� O(n), ���� ���� ���������������� (<1)


# 2. Formula
def summ_numbers_formula(n):
    return (n * (n + 1) / 2)

cProfile.run('summ_numbers_formula(1000000)')
#1    0.000    0.000    0.000    0.000 4_1.py:28(summ_numbers_formula) - 1 000 000
#1    0.000    0.000    0.000    0.000 4_1.py:28(summ_numbers_formula) - 10 000 000
#1    0.000    0.000    0.000    0.000 4_1.py:28(summ_numbers_formula) - 100 000 000

# ��������� ������, �.�. ������ ������� �� ������� �� n
# ��������� O(1)




