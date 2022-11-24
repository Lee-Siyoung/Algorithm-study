'''
그리드 문제로 2명이 최대한 적게 탈려면 가장 작은 사람과 가장 큰 사람 두명이 타야한다. 
처음에는 그냥 리스트로 했는데 효율성에서 하나가 실패해서 deque로 바꿔줬다.
'''
from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while len(people)>1:
        if people[0] + people[-1] <=limit:
            answer+=1
            people.pop()
            people.popleft()
        else:
            answer+=1
            people.pop()
    if people:
        answer+=1
    
    return answer