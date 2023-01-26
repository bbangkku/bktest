# sample_list = [11, 22, 33, 55, 66]

# #주어진 리스트의 3번 index에 있는 항목을 제거하고 변수에 할당해 주세요.
# # pop을 써보자 !

# print("original list: ", sample_list)

# elem = sample_list.pop(3)

# print("list after: ", sample_list)
# print(elem)

# # sample_list의 가장 뒤에 77을 추가해보세요

# sample_list.append(77)
# print("list after: ", sample_list)

# # 할당해놓은 변수의 값을 sample_list의 2번 index에 추가해보세요
# sample_list.insert(2, elem)
# print("list after: ", sample_list)

# my_tuple = (11, 22, 33, 44, 55, 66)

# # 주어진 튜플에서 44와 55의 값을 새로운 튜플에 할당해보세요.
# new_tuple = my_tuple[3: -1]
# print(new_tuple)

# test_list = [1, 2, 3, 7, 4, 6, 5]
# test_list.sort()
# print(test_list)

# scores = [('eng', 88), ('sci', 90), ('math', 80)]
# # 정렬
# print(scores)
# #키 값 기준 정렬
# scores.sort()
# print(scores)

# ### 중요
# # 점수 순으로 하고 싶다면 ? 함수를 만들어라
# def check(x):
# 	return x[1]
# #scores.sort(key=check) 이렇게 함수부터 3줄 !!! 써도되고
# # 람다사용 1줄에 가능 !!!
# scores.sort(key=lambda x: x[1])
# print(scores)
###############################################################복습
# 리스트 + 함수 에서의 복사

# 변수끼리의 복사
# 복사 후 값을 변경해도, 원본 값이 그대로 유지된다 > 깊은 복사(deep copy)
# 주소가 아닌, 값을 복사하는 경우
# a = 10
# b = a
# b = 20
# print(a)


# 함수 파라미터를 이해해야 함
# 함수에서의 복사
# def func(num):
# 	num += 10

# n = 10
# func(n)

# # 만약, 깊은 복사가 일어난다면 > 10 출력 <<< 이게맞는듯
# # 만약, 얕은 복사가 일어난다면 > 20 출력
# print(n)
# print(id(n))


# 리스트
a = [1, 2, 3]
# b = a
# b[0] = 10
# print(a)


# 리스트 깊은 복사 하는 방법 (값이 깊다 ! 값만 복사한다)
# # 얕은 복사 = 값까지 안들어가고 주소만 복사한다 ! 라는 느낌으로 암기
# a = [1, 2, 3]
# b = a.copy()
# b[0] = 10
# print(a)

# import copy
# a = [1, 2, [3, 4]]


# # 리스트 내부의 모든 복사를 깊은 복사로 변경
# b = copy.deepcopy(a)

# b[0] = 10

# print(a)
####################
# 람다 함수
li = [1, 4, 2, 3, 5, 3]

# 원본 함수를 변경 시켜 줌
li.sort()
li.sort(reverse=True)
# 정렬된 함수를 반환시켜 줌
new_li = sorted(li)

# 람다 함수
li = [[1, "가"], [2, "바"], [7, "다"], [5, "나"]]
# 젤 앞 요소를 순서대로 하고싶다.
li.sort()
# 두번쨰 요소를 순서대로하고싶다.
# 코드가 짧고 단순하다
# 다른 곳에서 안쓰인다. (일회용)
# - > 람다 함수(익명 함수)의 특징

# def func(x):
# 	return x[1]
# li.sort(key=func)

li.sort(key = lambda element: element[1])






print(li)
