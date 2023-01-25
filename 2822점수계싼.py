
from csv import list_dialects
from re import A
import sys
from collections import Counter
sys.stdin = open("./beak.txt","r")

# 리스트 만들기
scores = []
for i in range(8):
    n = int(input())
    scores.append(n)
scores_sort = sorted(scores)

#5개 값 뽑아내기
li = []
for i in range(3,len(scores_sort)):
    li.append(scores_sort[i])
max5 = scores_sort[3:]

print(sum(max5))

# 5개 값 원래 리스트에서 순서 추출하기
ind_li=[]
for j in range(5):
    ind_li.append(scores.index(max5[j])+1)

# 순서 정렬하기
for k in range(5):
    print(sorted(ind_li)[k], end=' ')

