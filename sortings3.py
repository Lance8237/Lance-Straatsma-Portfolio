import random
import math
import sys

sys.setrecursionlimit(5000)

def CreateRandomList(size):
    numbers = list(range(size))
    random.shuffle(numbers)
    return numbers 

def MakeMostlySortedData(size):
    A = CreateRandomList(size)
    A.sort()
    if len(A) > 1:
        A[0], A[-1] = A[-1], A[0]
    return A

def BubbleSort(A, work):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(len(A)-1):
            work["comparisons"] += 1
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                work["copies"] += 2
                sorted = False

def ShakerSort(A, work):
    sorted = False 
    while sorted == False:
        sorted = True
        for i in range(len(A)-1):
            work["comparisons"] += 1
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                work["copies"] += 2
                sorted = False
        for i in range(len(A)-2, -1, -1):
            work["comparisons"] += 1
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                work["copies"] += 2
                sorted = False

def CountingSort(A, work):
    max_val = max(A)
    F = [0] * (max_val + 1)
    
    for number in A:
        F[number] += 1
    
    k = 0
    for value in range(len(F)):
        count = F[value]
        for j in range(count):
            A[k] = value
            work["copies"] += 1
            k += 1

def QuickSort(A, low, high, work):
    if high - low <= 0:
        return
    
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        work["comparisons"] += 1
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            work["copies"] += 2
            lmgt += 1
    pivot_index = lmgt - 1
    A[low], A[pivot_index] = A[pivot_index], A[low]
    work["copies"] += 2
    QuickSort(A, low, pivot_index -1, work)
    QuickSort(A, pivot_index + 1, high, work)

def ModifiedQuickSort(A, low, high, work, modified):
    if high - low <= 0:
        return
    
    if modified:
        work["comparisons"] += 1
        mid = (low + high) // 2
        A[low], A[mid] = A[mid], A[low]
        work["copies"] += 2

        lmgt = low + 1
        for i in range(low + 1, high + 1):
            work["comparisons"] += 1
            if A[i] < A[low]:
                A[i], A[lmgt] = A[lmgt], A[i]
                work["copies"] += 2
                lmgt += 1
        pivot_index = lmgt - 1
        A[low], A[pivot_index] = A[pivot_index], A[low]
        work["copies"] += 2
        ModifiedQuickSort(A, low, pivot_index -1, work, True)
        ModifiedQuickSort(A, pivot_index + 1, high, work, True)

def MergeSort(A, work):
    if len(A) <= 1:
        return
    
    mid = len(A) // 2
    L = A[0:mid]
    R = A[mid:len(A)]

    MergeSort(L, work)
    MergeSort(R, work)

    i = 0
    j = 0
    k = 0

    while i < len(L) and j < len(R):
        work["comparisons"] += 1
        if L[i] < R[j]:
            A[k] = L[i]
            work["copies"] += 1
            i += 1
        else:
            A[k] = R[j]
            work["copies"] += 1
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        work["copies"] += 1
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        work["copies"] += 1
        j += 1
        k += 1

"""
#MAXIMS SOLUTION TO MERGESORT
def MaximMergeSort(A):

    #Base case
    if len(A) <= 1:
        return
    
    #split A into L and R
    mid = len(A) // 2
    L = A[0:mid]
    R = A[mid: len(A)]

    #Recurse
    MaximMergeSort(L)
    MaximMergeSort(R)

    #Merge L and R back into A
    for i in range(len(A)):
        if not R or (L and L[0] <= R[0]):
            A[i] = L.pop(0)
        else:
            A[i] = R.pop(0)

"""
            
def main():
    data = CreateRandomList

    if data == CreateRandomList:
        print("Counting work when sorting random data")
    else:
        print("Counting work when mostly sorted data")

    print("      Bubble  Shaker  Counting Merge  Quick  MQuick")

    size = 8
    while size <= 2048:
        log_size = math.log2(size)

        A = data(size)
        work = {"comparisons": 0, "copies": 0}
        BubbleSort(A, work)
        bubble_log = math.log2(work["comparisons"] + work["copies"])

        A = data(size)
        work = {"comparisons": 0, "copies": 0}
        ShakerSort(A, work)
        shaker_log = math.log2(work["comparisons"] + work["copies"])

        A = data(size)
        work = {"comparisons": 0, "copies": 0}
        CountingSort(A, work)
        counting_log = math.log2(work["comparisons"] + work["copies"])

        A = data(size)
        work = {"comparisons": 0, "copies": 0}
        QuickSort(A, 0, len(A) - 1, work)
        quick_log = math.log2(work["comparisons"] + work["copies"])

        A = data(size)
        work = {"comparisons": 0, "copies": 0}
        ModifiedQuickSort(A, 0, len(A) - 1, work, True)
        mquick_log = math.log2(work["comparisons"] + work["copies"])

        A = data(size)
        work = {"comparisons": 0, "copies": 0}
        MergeSort(A, work)
        merge_log = math.log2(work["comparisons"] + work["copies"])

        print(f"{log_size:02.0f}    {bubble_log:05.2f}   {shaker_log:05.2f}   "
              f"{counting_log:05.2f}    {merge_log:05.2f}  {quick_log:05.2f}  "
              f"{mquick_log:05.2f}")
        
        size *= 2
main()