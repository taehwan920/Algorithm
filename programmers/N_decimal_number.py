def solution(n, t, m, p):
    ready = ""
    for i in range(t*m):
        temp = ""
        while True:
            if i < n:
                temp += str(i % n) if i % n < 10 else up_ten(i % n)
                break
            temp += str(i % n) if i % n < 10 else up_ten(i % n)
            i //= n
        temp = list(temp)
        temp.reverse()
        ready += ''.join(temp)
    result = ""
    for i in range(p-1, len(ready), m):
        result += ready[i]
        if len(result) == t:
            return result


def up_ten(num):
    sample = ["A", "B", "C", "D", "E", "F"]
    return sample[num % 10]
# sorted(reverse=True와) reverse()가 다른걸 명심할 것.
