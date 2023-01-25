from csv import list_dialects
from re import A
import sys
from collections import Counter
sys.stdin = open("./beak.txt","r")

tc = int(input())

li = []
for i in range(tc):
    weight, height = map(int, input().split())
    li.append((weight,height))

answer = []
for i in range(tc):
    count = 0
    for j in range(tc):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            count +=1
    answer.append(count+1)

for k in answer :
    print(k, end= ' ')
    
