from itertools import combinations
def solution(numbers):
    answer = []
    numbers = list(combinations(numbers,2))
    for i in numbers:
        answer.append(sum(i))
    answer = sorted(list(set(answer)))
    return answer