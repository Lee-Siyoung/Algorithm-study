'''
일단 1같은 경우에 00001(2) 이 되어야 하는데 1이 되므로 zfill을 이용해 배열의 가장 큰 길이만큼 0을 넣도록 했다. 
'''
def solution(n, arr1, arr2):
    len1 = len(bin(max(arr1))[2:])
    len2 = len(bin(max(arr2))[2:])
    answer = []
    a1 = []
    a2 = []
    for i in arr1:
        a1.append(bin(i)[2:].zfill(len1))
    for i in arr2:
        a2.append(bin(i)[2:].zfill(len2))
    for a, b in zip(a1,a2):
        ans=''
        for i in range(len(a)):
            if a[i] == '1' or b[i] == '1':
                ans+='#'
            else:
                ans+=' '
        answer.append(ans)
    
    return answer