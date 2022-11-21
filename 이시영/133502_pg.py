'''
하나씩 넣다가 1,2,3,1이 뒤부터 체크했을때 나온다면 del로 없애주고 answer을 +1한다
'''
def solution(ingredient):
    answer = 0
    a=[]
    for i in ingredient:
        a.append(i)
        if a[-4:] == [1,2,3,1]:
            answer+=1
            del a[-4:]

            
    return answer