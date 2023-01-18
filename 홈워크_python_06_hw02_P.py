# A.    입력 예시 
a = ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

# b=''.join(sorted('tea'))
# result = {}

# result = {}
# for i in a:
#     b = ''.join(sorted(i))
#     result[b] = result.get(b,[]) + [i]
#     print(result)

def group_anagrams(a):
    result = {}
    for i in a:    
        b = ''.join(sorted(i))
        result[b] = result.get(b,[]) + [i]
    return result

print(group_anagrams(['eat','tea','tan','ate','nat','bat']))

