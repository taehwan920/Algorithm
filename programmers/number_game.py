def solution(A, B):
    A.sort()
    B.sort()
    score = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] < B[j]:
                score += 1
                B.pop(j)
                break
    return score

# pop을 해준뒤 break를 함으로써 인덱스 에러를 피하고 시간복잡도까지 낮출 수 있는 방법이 있었음.
# 정 인덱스 에러가 걱정이 된다면 for in range말고 그냥 for in을 사용해서 반복문을 돌리는 방법도 있다.
# 처음에 sort해서 같은 인덱스에 있는요소끼리 비교하는데 까지는 생각이 닿았는데
# 그게아니라 A요소를 작은것 부터 B의 요소와 비교해보며 B의 요소중 더 큰게 나오면 점수를 하나 더해주고 해당 B요소를 삭제하는 식으로 중복비교도 피하고, 시간 복잡도도 절약할 수 있었다.
