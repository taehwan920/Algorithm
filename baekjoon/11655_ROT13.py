get = input()

result = ''
for i in range(len(get)):
    now = get[i]
    if not now.isalpha():
        result += now
        continue

    if now.isupper():
        now = ord(now)
        now = now + 13 if now + 13 <= ord('Z') else now - 13
    else:
        now = ord(now)
        now = now + 13 if now + 13 <= ord('z') else now - 13
    result += chr(now)

print(result)
