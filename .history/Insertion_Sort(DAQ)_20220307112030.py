'''
Insertion Sort using Divide and Conquer Algorithm
Question can be divided into two parts, the first
1. Divide and Conquer
2. Insertion Sort
'''
from typing_extensions import Self


class DAC_IS ():
    def __init__(Self, arr, l, m, r):
        Self.arr = arr
        Self.l = int(l)
        Self.m = int(m)
        Self.r = int(r)

    def DAC(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def Insertion_Sort(arr, l, r):
        #print(r)
        print(l)
        if l < r :
            m = l+(r-l)//2
            Self.Insertion_Sort(arr, l, m)
            Self.Insertion_Sort(arr, m+1, r)
            Self.DAC(arr, l, m, r)
    
# Driver Code
sort = DAC_IS
unsorted_list = [12, 11, 13, 5, 6, 7]
n = len(unsorted_list)
#print(unsorted_list, "\n", n)
l = int(0)
sort.Insertion_Sort(unsorted_list, l, n-1)
print("Sorted array is: ")
for i in range(n):
    print(unsorted_list[i], end = " ")