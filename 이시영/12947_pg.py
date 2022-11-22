def solution(x):
    sum=0
    x_str = str(x)
    
    for i in x_str:
        sum+=int(i)
        
    if x%sum==0:
        return True
    return False