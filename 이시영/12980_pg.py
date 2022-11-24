'''
문제가 길지만 결국 (현재까지 온 거리)*2는 2로 나눠질때 순간이동하고 2로 나눠지지 못하면 점프하는 것이다.
'''
def solution(n):
    ans = 0
    
    while n:
        if n%2==0:
            n=n//2
        else:
            n-=1
            ans+=1
    
    return ans