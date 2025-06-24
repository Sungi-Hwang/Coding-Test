
def solution(schedules, timelogs, startday):
    lens = len(schedules)

    answer = 0
    for i in range(0, lens):
        Flag = True
        temp_startday = startday
        check_schedules = schedules[i]+10
        if check_schedules%100 >= 60:
            check_schedules = check_schedules+40
        for j in timelogs[i]:
            
            if temp_startday == 6 or temp_startday==7:
                temp_startday = temp_startday + 1;
                continue
            if check_schedules < j:
                print(i)
                print(j)
                print(temp_startday)
                Flag = False
                break
            temp_startday=temp_startday+1
            if temp_startday > 7:
                temp_startday -=7
            
        if Flag == True:
            answer = answer+1
    
    return answer
