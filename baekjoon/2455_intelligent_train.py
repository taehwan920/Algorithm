people = 0
most = 0
for i in range(4):
    off, on = map(int, input().split(' '))
    people -= off
    people += on
    if people > most:
        most = people

print(most)
