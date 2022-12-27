'''
numbers에서 다음값을 더한 값 or 뺀 값으로 트리를 구성한다.
[4, 1, 2, 1]일때의 경우로 다음 수를 빼고 더해서 결국 target일때 개수를 구한다.
'''
def solution(numbers, target):
    answer=0
    
    def dfs(numbers, target, sums, index):
        if index==len(numbers):
            if sums==target:
                nonlocal answer
                answer+=1
            return

        dfs(numbers,target,sums+numbers[index],index+1)
        dfs(numbers,target,sums-numbers[index],index+1)
    
    dfs(numbers,target,0,0)
    return answer