'''
dfs문제로 visited로 방문처리를 해준다. 
visited가 False이고 노드가 1이면 계속 dfs를 돌려 노드가 연결되었다면 answer를 +1해준다.
'''
def dfs(n, computers, start, visited):
    visited[start]=True
    for i in range(n):
        if visited[i]==False and computers[start][i]==1:
            visited = dfs(n,computers,i,visited)
    return visited

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for start in range(n):
        if visited[start]==False:
            dfs(n,computers,start,visited)
            answer+=1
    
    return answer