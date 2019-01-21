def insertionSort1(n, arr):
    last_num = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i]>last_num:
            arr[i+1] = arr[i]
            print(' '.join([str(x) for x in arr]))
        else:
            arr[i+1] = last_num
            print(' '.join([str(x) for x in arr]))
            break
    if last_num not in arr:
        arr[0] = last_num
        print(' '.join([str(x) for x in arr]))


insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
#insertionSort1(14, [1, 3, 5, 9, 13, 22, 27, 35, 46, 51, 55, 83, 87, 23])