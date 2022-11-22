'''
스테이지에 도달하지 못한 사용자를 del로 사용자의 개수만큼 없애고 실패율을 answer에 넣는다. 
그리고 정렬하는데 key값을 실패율의 내림차순으로 하는데 중복되면 스테이지가 작은 순으로 정렬하게 했다.
'''
def solution(N, stages):
    answer = []
    a=[]
    stages = sorted(stages)
    counts = len(stages)
    for i in range(1,N+1):
        if i in stages:
            a = stages.count(i)
            del stages[stages.index(i):stages.index(i)+a]
            answer.append([i,a/counts])
            counts = len(stages)
        else :
            answer.append([i,0])
    answer = sorted(answer, key= lambda x : (-x[1], x[0]))
    a = [x[0] for x in answer]
    return a