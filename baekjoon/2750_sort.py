nums = []

for _ in range(int(input())):
    nums.append(int(input()))


def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            break


def selection_sort(arr):
    for i in range(len(arr)-1):
        least = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[least]:
                least = j
        arr[i], arr[least] = arr[least], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        swapped = False
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                arr.insert(j+1, arr.pop(i))
                swapped = True
                break
        if not swapped:
            arr.insert(0, arr.pop(i))


# bubble_sort(nums)
selection_sort(nums)
# insertion_sort(nums)

for i in nums:
    print(i)
# n^2 시간복잡도 정렬 구현 문제
