# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, K = map(int, input().split())
N_arr = list(map(int, input().split()))

# if N == K:
# 	print(1)
# elif 2 * K > N:
# 	print(2)
# else:
# 	answer = N // (K-1)
# 	print(answer)

N_arr.remove(1)
N_arr.insert(0, 1)

count = 0
for i in range(1, N, K-1):
    count += 1

print(count)
