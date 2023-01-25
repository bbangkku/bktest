# count_vowels('apple') #=> 2
# count_vowels('banana') #=> 3

# a e i o u 

def count_vowels(n):
    count = 0 
    for word in n:
        if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':

            count += 1
            # print(count)
    return count

print(count_vowels('apple')) #=> 2
print(count_vowels('banana'))