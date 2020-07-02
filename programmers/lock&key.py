from copy import deepcopy


def solution(key, lock):
    additional = len(key) - 1
    new_lock = []
    for i in range(2 * additional + len(lock)):
        temp = []
        for j in range(2 * additional + len(lock)):
            if additional <= i <= additional + len(lock) - 1:
                if additional <= j <= additional + len(lock) - 1:
                    temp.append(lock[i - additional][j - additional])
                else:
                    temp.append(0)
            else:
                temp.append(0)
        new_lock.append(temp)

    def search(y, x):
        for t in range(4):
            limit += 1
            temp_key = deepcopy(key) if t == 0 else rotate(deepcopy(key))
            virtual_lock = deepcopy(new_lock)

            for i in range(y, y + len(key)):
                for j in range(x, x + len(key)):
                    virtual_lock[i][j] = temp_key[i-y][j-x]

            correct = False
            for i in range(additional, additional + len(key)):
                for j in range(additional, additional + len(key)):
                    if virtual_lock[i][j] == 0:
                        break
                else:
                    correct = True
                if correct:
                    return True

            return False

    def rotate(arr):
        return [[arr[j][i] for i in reversed(range(len(arr)))] for i in range(len(arr))]

    for i in range(len(new_lock) - additional):
        for j in range(len(new_lock) - additional):
            if search(i, j):
                return True
    return False

# lock 배열을 key의 길이에서 1뺀만큼 확장시켜서 한번씩 돌려가며 대조해보는 식으로 풀었는데.. TC의 1/3 가량이 틀렸다고 나왔다.
