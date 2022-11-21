def solution(s):
    answer = ''
    a=''
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in s:
        a+=i
        if a in num:
            answer+=i
            a=''
        elif a in number:
            answer+=str(number.index(a))
            a=''
        
    
    return int(answer)