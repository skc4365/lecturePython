import numpy as np

#arrNum = np.array([7, 5, 1, 4, 6, 3, 2], int)
#arrNum = np.array([5, 3, 8, 4, 9, 1, 6, 2, 7], int)
arrNum = np.array([54, 34, 41, 89, 67, 16, 52, 23], int)

def partition(arr, left, right):
    low = left +1
    high = right
    pivot = arr[left]
    print("pivot값 : {}, _low값: {}, high값: {}" .format(pivot, arr[low], arr[high]))
    print("pivot인덱스 : [{}], _low인덱스: [{}], high인덱스: [{}]" .format(left, low, high))
    
    while (low <= high):
        while low <= right and arr[low] < pivot:
            low += 1
            print("_LOW카운트: [{}]" .format(low))
        while high >= left and arr[high] > pivot:
            high -= 1
            print("_HIGH카운트: [{}]" .format(high))
            
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
            print("교환: {}" .format(arrNum))
            
    arr[left], arr[high] = arr[high], arr[left]
    print("파티션결과 : ", arrNum, "\n")
    
    print("high값 : {}, high인덱스: [{}]" .format(arr[high], high))
    return high
    
def sortQuick(arr, left, right):
    if left < right :
        print("partition(arr, left, right)파티션진행중...")
        p = partition(arr, left, right)
        print("sortQuick(arr, left, p - 1)왼쪽파티션_함수진행")
        sortQuick(arr, left, p - 1)
        print("sortQuick(arr, p + 1, right)오른쪽파티션_함수진행")
        sortQuick(arr, p + 1, right)
        

#_____ 출력
print("기본데이터: {}" .format(arrNum))
print("===============================")
#print("pivot값_________________: {}" .format(arrNum[0]))
sortQuick(arrNum, 0, len(arrNum)-1)
print("===============================")
print("퀵정렬 수행결과\n{}" .format(arrNum))
