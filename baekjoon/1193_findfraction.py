N = int(input())

count = 1

while N - count > 0:
    N = N - count
    count += 1

end = N

if count % 2 == 1:
    son = count - end + 1
    mother = end
else:
    son = end
    mother = count - end + 1

son = str(son)
mother = str(mother)

print(f"{son}/{mother}")
