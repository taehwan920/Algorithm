def solution(gems):
    gem_nums = len(set(gems))
    start, end = 0, 0
    get_gems = {gems[0]: 1}
    answer = [0, len(gems)]

    while start < len(gems) and end < len(gems):
        if len(get_gems) == gem_nums:
            if end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1]

            if get_gems.get(gems[start]):
                get_gems[gems[start]] -= 1

            if get_gems[gems[start]] == 0:
                del get_gems[gems[start]]

            start += 1
        else:
            end += 1

            if end == len(gems):
                break

            if get_gems.get(gems[end]):
                get_gems[gems[end]] += 1

            else:
                get_gems[gems[end]] = 1

    return answer
