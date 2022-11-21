'''

'''

def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*':[3, 0], 0: [3, 1], '#': [3, 2]
             }
    left = keypad['*']
    right = keypad['#']
    
    for i in numbers:
        a = keypad[i]
        if i in [1,4,7]:
            answer+='L'
            left = a
        elif i in [3,6,9]:
            answer+='R'
            right = a
        else:
            le, ri = 0,0
            for i, j, k in zip(left, right, a):
                le += abs(i-k)
                ri += abs(j-k)
            if le == ri:
                if hand == 'right':
                    answer+='R'
                    right = a
                else:
                    answer+='L'
                    left = a
            elif le>ri:
                answer += 'R'
                right = a
            elif le<ri:
                answer += 'L'
                left = a
                    
    return answer