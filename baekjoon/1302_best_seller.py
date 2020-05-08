N = int(input())

books = {}

for i in range(N):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

bk_li = sorted(books.items(), key=lambda x: x[0], reverse=True)
bk_li = sorted(bk_li, key=lambda x: x[1])
print(bk_li[-1][0])
