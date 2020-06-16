def solution(s):
    n = len(s)
    shortest = len(s)
    # 압축한 문자열 중 가장 짧은 것의 길이를 저장할 변수
    for i in range(1, n+1):
        temp = ''
        last = [0, '']
        # 반복문 실행 시 이전 슬라이싱한 문자열과 같은지 비교를 해야하기 때문에 [같은 문자열의 개수, 문자열]을 저장해준다.
        for j in range(0, n, i):
            if j == 0:
                last = [1, s[j:j+i]]
                # 첫 반복때는 last에 저장만해주고 넘어간다
                continue
            if s[j:j+i] == last[1]:
                # 만약 현재 슬라이싱한 문자열이 이전 슬라이싱 문자열과 같을 경우
                last[0] += 1
                # 해당 문자열의 개수만 하나 더해준다
            else:
                # 이전 슬라이싱 문자열과 다를 경우
                if last[0] > 1:
                    # 개수가 1보다 클 경우 앞에 숫자를 붙여줌
                    temp += f"{last[0]}{last[1]}"
                else:
                    # 개수가 1일경우 숫자를 붙이지 않음
                    temp += f"{last[1]}"
                # 이전 문자열과 다를 경우이므로 last를 갱신해준다.
                last = [1, s[j:j+i]]
        if last:
            # 반복문이 끝나면 마지막으로 슬라이싱된 문자는 비교가 안되므로 마지막 슬리이싱 문자를 같이 temp에 넣어주는 과정을 추가. 로직은 반복문때와 같다.
            if last[0] > 1:
                temp += f"{last[0]}{last[1]}"
            else:
                temp += f"{last[1]}"
        shortest = len(temp) if len(temp) < shortest else shortest
        # 더 짧은 길이를 shortest에 저장
    return shortest

# 전에 한번 도전했다 손도 못대고 포기해서 겁먹고 안 건들고 있다가 막상 다시 풀어보니 생각보다 쉬워서 허탈했던 문제.
# 문자열 다루기 그 자체에 얼마나 익숙한지를 테스트하는 문제다.
# 문자열 슬라이싱은 len(s) = 10 일때 s[a:b]로 슬라이싱하는데 b가 만약 10보다 크다고 하더라도 인덱스 에러가 뜨거나 하지않고 그냥 있는글자까지만 나옴.
# 그래서 압축하는 문자열 길이를 1부터 시작해서 1씩 늘려가며 압축된 걸 길이를 비교하면된다.
