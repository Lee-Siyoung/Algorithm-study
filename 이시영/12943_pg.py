'''
만약 테스트 케이스13만 틀렸다면 입력값이 1일때를 상정안해서 그렇다.
'''
def solution(num):
    answer = 0
    while True:
        if num == 1:
            return answer
        if answer ==500:
            return -1
        if num%2==0:
            num = num//2
        else:
            num = num*3+1
        answer+=1
