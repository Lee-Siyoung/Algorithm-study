'''
capitalize()는 문자열의 첫 글자를 대문자로 나머지는 소문자로 바꿔준다.

여러개가 있는데

capitalize() - 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환한다.

title() - 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환한다.

ucfirst() - 문자열의 첫글자는 대문자로 변환하고, 나머지는 그대로 둔다. 얘는 내장함수가 아니다.
'''

def solution(s):
    answer = ''
    s = s.split(' ')
    for i in s:
        answer+=i.capitalize() + ' '
    return answer[:-1]