from csv import list_dialects
from re import A
import sys
from collections import Counter
sys.stdin = open("./beak.txt","r")

# while True:
# n=list(map(int,(input())))
# new_n = []
# while n == new_n:
#     list(map(int,(n[0] + n[1]))) == new_n.append()
# print(new_n)

n= int(input())
# print(n)
sum = 0 
count = 0
while str(n) == str(sum):
    for word in str(n):
        int_word = int(word)
        sum = sum + int_word
        count = count + 1
        word = str(sum)

print(word)
        

        



