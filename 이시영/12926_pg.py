def solution(s, n):
    answer = ''
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            if ord(i)+n >90:
                answer+= chr(ord(i)+n-26)
            else:
                answer+= chr(ord(i)+n)
        elif ord(i) >= 97 and ord(i) <= 122:
            if ord(i)+n >122:
                answer+= chr(ord(i)+n-26)
            else:
                answer+= chr(ord(i)+n)
        else:
            answer+=' '
    return answer