t = int(input())
for _ in range(t):
    say = input().split()

    while True:
        what = input().split()[-1]
        if what == 'say?':
            break
        for i in range(len(say)):
            if say[i] == what:
                say[i] = ''

    say = list(filter(lambda x: x != '', say))
    print(' '.join(say))
