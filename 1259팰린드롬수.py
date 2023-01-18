from csv import list_dialects
from re import A
import sys
from collections import Counter
sys.stdin = open("./baek.txt","r")


while True:
    n=list(map(int,(input())))
    
    if n==[0]:
        break
    for i in n:
        s = "yes"
        for j in range(len(n)):
            
            if n[j]==n[-1-j]:
                pass
            else:
                s = "no"
    print(s)



        