'''
h번 이상 인용되었다는것은 오름차순으로 정렬하면 하나의 값 i번 뒤에는 다 i번 이상 인용되었다는 것과 똑같다.
'''
def solution(citations):
    answer=0
    citations = sorted(citations)
    for i in range(len(citations)):
        count = len(citations)-i
        if citations[i] >= count:
            answer= count
            break
    return answer