sample = input().split()
end = [str(i) for i in range(1, 6)]

while sample != end:
    for i in range(4):
        if sample[i] > sample[i+1]:
            sample[i], sample[i+1] = sample[i+1], sample[i]
            print(' '.join(sample))
