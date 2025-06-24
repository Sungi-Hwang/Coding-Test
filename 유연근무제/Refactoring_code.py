def add_ten_minutes(hhmm):
    """HHMM 형식에 10분을 더하는 함수"""
    hour, minute = divmod(hhmm, 100)
    minute += 10
    if minute >= 60:
        hour += 1
        minute -= 60
    return hour * 100 + minute

def is_weekday(day):
    """1~5는 평일, 6~7은 주말"""
    return day not in (6, 7)

def advance_day(day):
    """요일 증가 (1~7 → 1:월, ..., 7:일)"""
    return 1 if day == 7 else day + 1

def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        current_day = startday
        deadline = add_ten_minutes(schedules[i])

        for log in timelogs[i]:
            # 주말이면 건너뜀
            while not is_weekday(current_day):
                current_day = advance_day(current_day)

            if log > deadline:
                # 출근 시간이 10분 초과 → 실패
                break

            current_day = advance_day(current_day)
        else:
            # 모든 근무일에 출근 성공
            answer += 1

    return answer
