import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
my_card = list(map(int, input().split()))
m = int(input())
sample = list(map(int, input().split()))
my_card.sort()


def BST1(li, num):
    if len(li) == 1:
        return 1 if li[0] == num else 0
    mid = len(li) // 2
    if li[mid] == num:
        return 1
    elif li[mid] < num:
        if len(li) == 2:
            return 0
        else:
            return BST1(li[mid + 1:], num)
    else:
        return BST1(li[:mid], num)


for i in range(len(sample)):
    print(BST1(my_card, sample[i]), end=" ")
# 내가 푼 것. 시간초과 or 메모리초과가 계속 떠서 풀 수가 없었음.

input = sys.stdin.readline

n = int(input())
my_card = list(map(int, input().split()))
m = int(input())
sample = list(map(int, input().split()))
my_card.sort()


def BST(num):
    s = 0
    e = n - 1
    while s <= e:
        mid = (s + e) // 2
        if my_card[mid] == num:
            return 1
        elif my_card[mid] > num:
            e = mid - 1
        else:
            s = mid + 1
    return 0


for i in range(len(sample)):
    print(BST(sample[i]), end=" ")

# 고친 것. 당연히 재귀가 더 빠르겠지 싶어서 재귀로 풀었었는데 그게 패인이었던 것같다. 하던거나 잘 하자.
