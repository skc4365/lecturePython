import numpy as np

#arrNum = np.array([7, 5, 1, 4, 6, 3, 2], int)
#arrNum = np.array([5, 3, 8, 4, 9, 1, 6, 2, 7], int)
arrNum = np.array([54, 34, 41, 89, 67, 16, 52, 23], int)

def partition(arr, left, right):
    low = left +1
    high = right
    pivot = arr[left]
    print("pivot값===================: {}" .format(arr[left]))
    
    print("_low: {}, high: {}" .format(arr[low], arr[high]))
    while (low <= high):
        while low <= right and arr[low] < pivot:
            low += 1
        while high >= left and arr[high] > pivot:
            high -= 1
            
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
            print("교환: {}" .format(arrNum))
            
    arr[left], arr[high] = arr[high], arr[left]
    print("교환결과_____: ", arrNum)
    
    print("high값______________: {}" .format(arr[high]))
    return high
    
def sortQuick(arr, left, right):
    if left < right :
        p = partition(arr, left, right)
        sortQuick(arr, left, p - 1)
        sortQuick(arr, p + 1, right)
        

#_____ 출력
print("기본데이터: {}" .format(arrNum))
print("===============================")
#print("pivot값_________________: {}" .format(arrNum[0]))
sortQuick(arrNum, 0, len(arrNum)-1)
print("===============================")
print("퀵정렬 수행결과\n{}" .format(arrNum))
