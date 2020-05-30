def solution(record):
    logs = {}
    order = []
    for i in record:
        temp = list(i.split(' '))
        if temp[0] == 'Leave':
            logs[temp[1]]['log'].append(temp[0])
            order.append(temp[1])
        if temp[0] == 'Enter':
            if temp[1] in logs:
                logs[temp[1]]['log'].append(temp[0])
                logs[temp[1]]['name'] = temp[2]
            else:
                logs[temp[1]] = {'log': ['Enter'], 'name': temp[2]}
            order.append(temp[1])
        if temp[0] == 'Change':
            logs[temp[1]]['name'] = temp[2]
    result = []
    while order:
        temp = order.pop(0)
        t_log = logs[temp]['log'].pop(0)
        if t_log == "Enter":
            result.append(f"{logs[temp]['name']}님이 들어왔습니다.")
        if t_log == "Leave":
            result.append(f"{logs[temp]['name']}님이 나갔습니다.")
    return result
