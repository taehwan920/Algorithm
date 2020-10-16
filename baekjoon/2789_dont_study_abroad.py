sample = input()
censor = {i: 1 for i in "CAMBRIDGE"}

result = ''
for c in sample:
    if not censor.get(c):
        result += c

print(result)
