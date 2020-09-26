def binarySearch1(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1
    # 가장 기본적인 형태
    # 문제 풀이가 배열 내 요소의 인접 여부와 상관없을 때 쓰임.
    # 각 단계 별로 후처리가 요구되지 않는 경우에 사용. element를 찾기 위해 사용


def binarySearch2(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1
    # 응용 형태
    # 문제 풀이 시 각 요소의 오른쪽 요소에 접근해야할 때 사용.
    # 현재 가리키고있는 요소의 오른쪽 요소가 조건을 만족하는지 여부에 따라 왼쪽 혹은 오른쪽으로 갈지 결정할 때 사용.
    # 각 단계 별로 탐색해야하는 요소가 최소 2개 이상인 경우
    # 바로 위의 이유로 요소가 1개 남았을 때 반복문을 종료해야 하는 경우. && 남은 요소가 조건을 만족하는 지 검증해야함.


def binarySearch3(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1

    # 또 다른 응용 형태
    # 탐색 조건이 현재 가리키고있는 요소의 양 옆 요소에 접근해야하는 경우
    # 현재 가리키고있는 요소의 옆 요소를 사용하여 조건 충족 여부를 판단하고, 왼쪽 혹은 오른쪽 중 어디로 갈 지 판단할 때
    # 탐색 범위가 최소 3 이상일 때
    # 후처리 필요. 반복문은 남은 요소가 2개일 때 종료. && 남은 요소가 조건을 만족하는 지 검증해야함.
