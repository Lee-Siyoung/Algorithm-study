'''
Counter 함수로 개수를 센 뒤 most_common()을 이용해 개수가 많은 순으로 정렬을 시켜준 뒤 
array이 하나일땐 일단 그대로 맨 앞에 있는것을 return해주고 
만약 앞과 뒤의 개수가 같다면 최빈값이 여러개 있다는 뜻이므로 -1을 return해준다. 
'''

from collections import Counter
def solution(array):
    array =Counter(array).most_common()
    if len(array) == 1:
        return array[0][0]
    if array[0][1] == array[1][1]:
        return -1
    return array[0][0]