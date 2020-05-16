def solution(msg):
    dic = [0] + [chr(i) for i in range(ord('A'), ord('Z')+1)]
    result = []
    skip = 0
    last = False
    for i in range(len(msg)-1):
        num = 1
        if skip:
            skip -= 1
            continue
        while msg[i:i + num] in dic:
            if i + num == len(msg):
                last = True
                break
            num += 1
        if last:
            result.append(dic.index(msg[i:i + num]))
            break
        else:
            result.append(dic.index(msg[i:i + num - 1]))
            dic.append(msg[i:i + num])
            skip = num - 2
    if not(last):
        result.append(dic.index(msg[-1]))
    return result

# 1. 먼저 A-Z까지 리스트를 만들고, 결과를 담을 배열 result를 선언.
# 2. skip은 검색한 문자열이 두 글자 이상일 경우 그 문자열에 포함되어있던 문자를 스킵해야 하므로 스킵할 글자 수를 저장할 변수.
# 3. last는 마지막 검색 문자열이 두글자 이상일 경우, 반복문 탈출 조건을 마련하기 위한 변수.
# 4. for 반복문은 맨 마지막 글자를 제외한 ( 항상 다음 글자 포함한 문자열도 검색을 해야하므로 ) 모든 문자를 한번 씩 돌도록 했음.
# 5. num 변수는 다음 글자를 검색하기 위한 정수 변수. 혹시 skip해야하는 글자가 있는 경우 skip.
# 6. while문은 사전에 없는 문자열 (msg의 현재 글자 + 다음 글자인 문자열)이 나올 때 까지 num을 1씩 늘려 검색하는 글자 수를 점점 늘림.
# 7. 만약 검색하는 문자열이 msg의 마지막 글자까지 포함함 && 사전에 등록돼있음 => last를 True로 바꾸고 반복문 탈출.
# 8. 7번의 로직에서 연결돼서 나온 조건식. 그러면 result 배열에 사전 인덱스를 넣어줌.
# 9. 7, 8번에 해당하지 않는 경우, 현재 입력된 문자열의 사전 인덱스를 result에 넣고, 다음 글자(c, 문제 참조)까지 포함한 글자를 사전에 새로 추가함.
# 10. skip변수는 사전에서 검색한 문자열의 글자 수가 2글자 이상일 경우, num이 3이상이기 때문에 다음과 같이 선언. 만약 2글자일 경우, 다음 글자는 스킵하고 그 다음 글자를 검색하게 된다.
# 11. for 반복문이 끝났는데도 마지막 문자열을 핸들링한 적 없는 경우, 마지막 문자열의 사전 인덱스를 result에 추가해주고 끝난다.
