'''
lambda를 이용해 일단 strings[n]을 기준으로 정렬하고 그 다음 같을때 strigns을 기준으로 한다.
'''
def solution(strings, n):
    return sorted(strings, key = lambda x : (x[n], x))