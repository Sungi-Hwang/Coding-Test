def make_total_code(n):
    total_code = []
    for i in range(1 , n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for x in range(k+1, n-0):
                    for y in range(x+1, n+1):
                        total_code.append([i,j,k,x,y])
    return total_code
def match_count_check(code, key, match_num):
    num = 0
    flag = False
    for i in range(0, len(key)):
        if (key[i] in code) == True:
            num+=1
    if num == match_num:
        flag = True

    return flag
def solution(n, q, ans):
    total_code = []
    total_code = make_total_code(n)
    max_index = len(total_code)
    uncorrect_num = 0
    flag = True
    for i in range(0, max_index):
        for j in range(0, len(q)):
            flag = match_count_check(total_code[i],q[j],ans[j])
            if flag == False:
                uncorrect_num += 1
                flag = True
                break
    print(total_code[len(total_code)-1])
    answer = max_index-uncorrect_num
    return answer
