#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):

    i = 0
    swapped = True
    while i < len(A) - 1 and swapped:
        swapped = False
        for j in range(0, len(A) - 1 - i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                swapped = True
        i += 1

def insertionSort(A):
    for i in range(1, len(A)):
        j = i
        while (j>0) and (A[j-1] > A[j]):
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp
            j = j - 1
    

def selectionSort(A):
    for i in range(0, len(A) - 1):
        minIdx = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minIdx]:
                minIdx = j
        temp = A[minIdx]
        A[minIdx] = A[i]
        A[i] = temp


def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


