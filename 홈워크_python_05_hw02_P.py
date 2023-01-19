# fn_d(91) 
# 출력 예시 
# 101

# fn_d


# 91 > 9 + 1 + 91
a=91

# def fn_d(n):
    


# def fn_d(n):
#     b = str(n)
#     c = list((map(int, b)))
#     c.append(int(n))
#     sum = 0
#     for i in range(len(c)):
#         sum = sum + c[i]
#     return sum

# print(fn_d(123))
fn_d = lambda n: sum([int(c) for c in str(n)] + [n])
print(fn_d(31))

def is_selfnumber(n):
    return len([i for i in range(n) if fn_d(i) == n]) == 0
    

print(is_selfnumber(20))







