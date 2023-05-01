def divide(arr, si, ei):
    if(si >= ei):
        return
    mid = si + (ei-si)/2
    divide(arr, si, mid)
    divide(arr, mid + 1, ei)
    conquer(arr, si, mid, ei)

def conquer(arr, si, mid, ei):
    merged = [] * (ei - si + 1)
    idx1 = si
    idx2 = mid + 1
    x = 0
    while idx1 <= mid and idx2 <= ei :
        if arr[idx1] <= arr[idx2]:
            merged(x++) = arr(idx1++)
        else:
            merged(x++) = arr(idx2++)

    while idx1 <= mid :
        merged[x++] = arr[idx1++]

    while idx2 <= ei :
        merged[x++] = arr[idx2++]
    
    j = si
    for i in range(len(merged)):
        arr[j] = merged[i]
        j += 1
#Driver Code

arr = [6, 3, 9, 5, 2, 8]
n = len(arr)

divide(arr, 0, n-1)

for i in range(n):
    print(arr[i], end = ' ')