grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]


# 금액 리스트 만들기
price = []
for keys in grain_lst:
    price.append(keys[1])

# 최고금액과 동일한 작물 추출
for keys in grain_lst:
    if keys[1] == max(price):
        print(keys[0])
    else:
        pass