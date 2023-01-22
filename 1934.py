from csv import list_dialects
from re import A
import sys
from collections import Counter
sys.stdin = open("./input1.txt")

a = list(map(int, input().split()))

def f(n):
    if n > 1 :
        return n*f(n-1)
    else:
        return 1    
print(f(a[0])//f(a[0]-a[1])//f(a[1]))
    

