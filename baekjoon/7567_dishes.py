sample = input()

result = 10
for i in range(1, len(sample)):
    if sample[i] == sample[i-1]:
        result += 5
    else:
        result += 10

print(result)
