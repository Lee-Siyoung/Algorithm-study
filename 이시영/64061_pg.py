def solution(board, moves):
    answer = 0
    bo=[]
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] ==0:
                pass
            else:
                bo.append(board[j][i-1])
                board[j][i-1]=0
                break
        if len(bo)>=2 and bo[-1]==bo[-2]:
            bo = bo[:-2]
            answer+=2
    return answer