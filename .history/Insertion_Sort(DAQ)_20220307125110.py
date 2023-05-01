'''
Insertion Sort using Divide and Conquer Algorithm
Question can be divided into two parts, the first
1. Divide and Conquer
2. Insertion Sort
'''

class DAC_IS ():
    def __init__(self, arr, l, m, r):
        self.arr = arr
        self.l = int(l)
        self.m = int(m)
        self.r = int(r)

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
        j1 = 0
        k = l
        """
Inertion sort Algorithm
1. create a value key
2. Compare the value key with preceding elements
3. If smaller found, insert it in between
4. Move the value to the next element.
        """
        for x in range(i, n1):
            value = L[x]
            j = x - 1
            if value < L[j]:
                while j>=0 and value < L[j]:
                    arr[j+1] = L[j]
                    j -= 1
                arr[j+1] = value
            else:
                arr[j] = L[j]
        
        for x in range(j1, n2):
            value = R[x]
            j = x - 1
            if value < R[j]:
                while j>=0 and value < R[j]:
                    arr[j+1] = arr[j]
                    j -= 1
                arr[j+1] = value
            else:
                arr[j] = R[j]
    '''
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
    '''
    def Insertion_Sort(arr, l, r):
        #print(r)
        if l < r :
            m = l+(r-l)//2
            DAC_IS.Insertion_Sort(arr, l, m)
            DAC_IS.Insertion_Sort(arr, m+1, r)
            DAC_IS.DAC(arr, l, m, r)
    
# Driver Code
sort = DAC_IS
unsorted_list = input("Enter the elements to be sorted:")
unsorted_list = unsorted_list.split(" ")
n = len(unsorted_list)
#print(unsorted_list, "\n", n)
sort.Insertion_Sort(unsorted_list, 0, n-1)
print("Sorted array is: ")
for i in range(n):
    print(unsorted_list[i], end = " ")