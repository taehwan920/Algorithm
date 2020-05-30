def solution(lines):
    logs = list(map(lambda x: to_obj(x), lines))
    result = []
    for i in logs:
        result.append(check(i['start_time'], logs))
        # 각 요소의 스타트타임부터 체크해보기
        result.append(check(i['end_time'], logs))
        # 각 요소의 엔드타임부터 체크해보기
    return max(result)


def check(time, li):
    cnt = 0
    start = time
    end = time + 999
    for i in li:
        if i['end_time'] >= start and i['start_time'] <= end:
            cnt += 1
    return cnt
    # 어느 시간대의
    # 리스트 내 각 요소 별로 시간대에 걸치는 놈들을 체크. 비교하고자 하는 시작 시간보다 각 요소의 종료 시간이 크거나 비교하고자 하는 종료 시간보다 각 요소의 시작시간이 작으면 카운팅해줌.


def to_obj(string):
    date, time, process = map(str, string.split(' '))
    process_time = int(float(process[:-1]) * 1000)
    h, m, s = map(float, time.split(":"))
    end_time = int(h * 3600000) + int(m * 60000) + int(s * 1000)
    start_time = end_time - process_time + 1
    return {
        'start_time': start_time,
        'end_time': end_time
    }
