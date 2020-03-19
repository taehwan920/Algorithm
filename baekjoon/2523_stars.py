N = int(input())

count = 1
how = True

while True:
    if count == 0:
        break
    elif count < N:
        print("*" * count)
        if how == True:
            count += 1
        else:
            count -= 1
    else:
        print("*" * count)
        how = False
        count -= 1
