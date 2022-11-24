'''
두수의 곱의 누적값이 최소로 되려면 A는 작은거 B는 큰거끼리 곱하면 된다.
'''
def solution(A,B):
    answer = 0

    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(len(A)):
        answer+=A[i]*B[i]
    return answer