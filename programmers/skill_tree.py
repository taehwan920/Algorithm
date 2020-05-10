def solution(skill, skill_trees):
    count = 0

    for i in range(len(skill_trees)):
        temp = list(filter(lambda x: x in skill, skill_trees[i]))
        temp_ck = [0] * len(temp)
        for j in range(len(temp)):
            if temp[j] == skill[j]:
                temp_ck[j] = 1
        if 0 not in temp_ck:
            count += 1

    return count
