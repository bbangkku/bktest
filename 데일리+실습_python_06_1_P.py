# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(n):
    return str(n)[:6]+'*******'



print(de_identify('9701034546545641234567'))

    
