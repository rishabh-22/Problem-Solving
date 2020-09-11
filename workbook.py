def workbook(n, k, arr):  # arr: 4 2 6 1 10
    book = []
    for i in range(1, n+1):
        page = []
        for q in range(1, (arr[i-1]+1)):
            page.append(q)
            if len(page) == k:
                book.append(page)
                page = []
        else:
            if page:
                book.append(page)
    print(book)
    print(len(book))

    count = 0
    for num in range(1, (len(book)+1)):
        if num in book[num-1]:
            count += 1

    print(count)


workbook(5, 3, [4, 2, 6, 1, 10])
