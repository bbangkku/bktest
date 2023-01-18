# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}


import calendar


import calendar

while True:
    year = int(input('연도를 입력해주세요 : '))
    if calendar.isleap(year) == True:
        print('윤년입니다. 연도를 다시 입력해주세요')
    else:
        print(calendar.calendar(year))
        break
month=int(input('월을 입력해주세요 : '))
day=int(input('일자를 입력해주세요 : '))
weekday = calendar.weekday(year,month,day)
if weekday == 0 :
    print("경고 월요일입니다.")
else : 
    pass

if weekday == 0 :
    weekday = '월요일'
elif weekday == 1 :
    weekday = '화요일'           
elif weekday == 2 :
    weekday = '수요일'   
elif weekday == 3 :
    weekday = '목요일'   
elif weekday == 4 :
    weekday = '금요일'   
elif weekday == 5 :
    weekday = '토요일'
else:
    weekday = '일요일'                                                                   
a = {'년' : year, '월' : month, '일': day, '요일' : weekday}
print(a)




