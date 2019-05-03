# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:54:07 2019

@author: ADMIN
"""

def lcs(a, b):
    c = [[-1]*(len(b) + 1) for _ in range(len(a) + 1)]
    lcs_two(a, b, c, 0, 0)
    return c
 
 
def lcs_two(a, b, c, i, j):
    if c[i][j] >= 0:
        return c[i][j]
 
    if i == len(a) or j == len(b):
        t = 0
    else:
        if a[i] == b[j]:
            t = 1 + lcs_two(a, b, c, i + 1, j + 1)
        else:
            t = max(lcs_two(a, b, c, i + 1, j),
                    lcs_two(a, b, c, i, j + 1))
    c[i][j] = t
    return t
 
 
def print_lcs(a, b, c):
    """Print one LCS of u and v using table c."""
    i = j = 0
    while not (i == len(a) or j == len(b)):
        if a[i] == b[j]:
            print(a[i], end='')
            i += 1
            j += 1
        elif c[i][j + 1] > c[i + 1][j]:
            j += 1
        else:
            i += 1
 
 
a = input('Enter first string: ')
b = input('Enter second string: ')
c = lcs(a, b)
print('Longest Common Subsequence: ', end='')
print_lcs(a, b, c)