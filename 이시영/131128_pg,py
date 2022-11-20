'''
set 함수 중 &은 교집합을 나타내주기 때문에 이걸 써서 같은 수를 골라내고 
Counter함수로 숫자의 개수를 구해 교집합에 나타난 숫자 중 작은것을 곱해 answer에 넣어준다.
'''
from collections import Counter
def solution(X, Y):
    nx, ny = (Counter(X)), (Counter(Y))
    setxy = sorted(set(X)&set(Y), reverse=True)
    
    if setxy:
        answer=''
        for i in setxy:
            answer += i * min(nx[i], ny[i])
        if sum(list(map(int,list(answer))))== 0:
            answer= '0'
        return answer    
    else:
        return '-1'