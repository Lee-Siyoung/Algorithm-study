'''
set성질을 이용해 중복을 없앤 것의 길이와 N//2를 해준 것중 최솟값을 구하면 된다.
'''
def solution(nums):
    a=list(set(nums))
    return min(len(a), len(nums)//2)