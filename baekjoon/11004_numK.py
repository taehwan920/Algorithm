n, k = map(int, input().split())

nums = list(map(int, input().split()))


def m_sort(li):
    if len(li) <= 1:
        return li

    center = int(len(li)/2)
    left = m_sort(li[:center])
    right = m_sort(li[center:])
    return merge(left, right)


def merge(l, r):
    l_count = 0
    r_count = 0
    merged = []
    while len(l) > l_count and len(r) > r_count:
        if l[l_count] > r[r_count]:
            merged.append(r[r_count])
            r_count += 1
        else:
            merged.append(l[l_count])
            l_count += 1

    while len(l) > l_count:
        merged.append(l[l_count])
        l_count += 1

    while len(r) > r_count:
        merged.append(r[r_count])
        r_count += 1
    return merged


_nums = m_sort(nums)
print(_nums[k-1])
