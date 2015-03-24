def insertion_sort(a):
    for to_sort, i in zip(a, range(len(a))):
        j = i-1
        while j>=0 and a[j] > to_sort:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = to_sort
    return a
