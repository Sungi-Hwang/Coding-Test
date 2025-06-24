import numpy as np
def solution(k, d):
    check = 0
    answer= 0 
    temp = np.arange(0,d+k ,k)
    j = 0
    anyway = d**2
    for i in range(0, d+1, k):
        temp = anyway - i**2
        temp_int = int(np.sqrt(temp))
        answer += temp_int//k+1

    return answer
