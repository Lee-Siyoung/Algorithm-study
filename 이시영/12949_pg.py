'''
행렬의 곱셈 중 *을 사용하지 않고 @를 하는데 이유는 *는 가로 세로가 같아야하지만 @는 2,3 3,2처럼 달라도 된다.
'''
import numpy as np
def solution(arr1, arr2):
    arr1=np.array(arr1)
    arr2=np.array(arr2)
    return (arr1@arr2).tolist()