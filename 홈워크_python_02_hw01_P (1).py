orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
li = orders.split(',')
print("주문수 : ",len(li))
se = set(li)
li1 = list(se)
li1.sort(reverse = True)
# print("중복 제거 메뉴 : ",li1)
for i in range(len(li1)):
    li_count = li.count(li1[i])
    print(li1[i],li_count,"개")
    