# -*- coding: utf-8 -*-
"""
Created on Fri April 26 11:23:16 2019

@author: ADMIN
"""

def initial (string, string_b):
    a = string_b
    if same (string,a):
        return True
    
    for j in range(2,len(a)):
        for i in range (len(a)-j +1):
            if same (string, a[i: i+j]):
                return True
    return False
    
def same (s1,s2):
    m = [[False for a in range (len(s2)+1)]
    for y in range (len(s1)+1)]
    m[0][0] = True
    
    for i in range(1,len(s1)+1):
        for j in range (1, len(s2)+1):
            if(s2[j-1]==s1[i-1]) or (s2[j-1] == "."):
                m[i][j] = m [i-1][j-1]
            elif (s2[j-1] == "*"):
                if((s2[j-2]==".") or (s2[j-2] == s1[i-1])):
                    m[i][j] = m[i-1][j] | m[i][j-1]
            else:
                m[i][j] = False
    
    if (s2 == 'a*aba**d'):
        print(m)
    return m [len(s1)][len(s2)]

def main():
    s1 = input("Enter first string:")
    s2 = input("Enter second string:")
    print(initial(s1,s2))
    
main()