def mergeSort(a,b):
    # "a" and "b" are both sorted arrays 
    # The efficiency has to be nlog(n) or more efficient
    i = 0
    j = 0
    count = 0
    c = []
    while 1:
        count+=1
        if a[i] <= b[j]:
            c.append(a[i])
            i = i + 1
            if i == len(a):
                c = c + b[j:]
                break
        else:
            c.append(b[j])
            j = j + 1
            if j == len(b):
                c = c + a[i:]
                break
        if len(c) == len(a) + len(b):
            break
    print(f"Loop ran {count} times!!")
    return c