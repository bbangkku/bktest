# sum_of_digit(3904) # 16

def sum_of_digit(n):
    li_n = list(map(int,list(str(n))))
    return sum(li_n)


def sum_of_digits(n):
    li_n = list(map(int,list(str(n))))
    sum = 0
    for i in range(len(li_n)):
        sum = sum + li_n[i]
    return sum

def sum_of_digitss(n):
    sum = 0
    int_n = int(n)
    while int_n>0:
        sum = (int_n % 10) + sum
        int_n = int_n // 10
    return sum
    # return sum

            # print(int_n)

        # return sum


print(sum_of_digit(3904))
print(sum_of_digits(3904))
print(sum_of_digitss(3904))




