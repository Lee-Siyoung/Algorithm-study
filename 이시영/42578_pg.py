'''
해시문제라 되어있는데 그냥 수학문제이다. 옷을 조합할 때 입을 경우, 안입을 경우가 있기때문에 (옷+1) * (옷+1) ...  -1 을 해준다. 
여기서 -1을 해주는 이유는 최소 하나의 옷을 입기 때문에 아예 안입는 경우는 제외해준다.
'''
def solution(clothes):
    answer = 1
    a = {i[1] : [] for i in clothes}
    
    for i in clothes:
        a[i[1]].append(i[0])

    cou=list(map(len, a.values()))
    for i in cou:
        i+=1
        answer*=i
        
    
    return answer-1