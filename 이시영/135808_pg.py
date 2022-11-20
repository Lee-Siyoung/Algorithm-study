'''
여기서 k는 딱히 생각안해도 된다. 
높은 것부터 정렬한 후 어차피 분류한 것 중 제일 작은 점수에 *m을 하기 때문에 m-1부터 m씩 건너면 작은 것들만 골라가기 때문에 저기서 answer을 더한다.
'''
def solution(k, m, score):
    answer = 0
    
    score = sorted(score, reverse=True)
    for i in range(m-1, len(score), m):
        answer+=score[i]*m
    
    return answer