def solution(arr1, arr2):
    result = []

    for i in range(len(arr1)):
        temp_a = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr2)):
                temp += arr1[i][k] * arr2[k][j]
            temp_a.append(temp)
        result.append(temp_a)
    return result

# 구현문제는 문제 속에 답이 있으니 안풀린다면 다시 잘 읽어보고, range의 크기는 고정된 값으로 입력할것.. arr2[i]와 arr2[0]은 다름
