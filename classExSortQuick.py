import numpy as np

#===== 퀵 정렬 =====
# arrNum = np.array([57, 33, 41, 91, 7, 18, 52, 23], int)
# 예제는 홀수개를 준비하여, 정가운데 4를 pivot이라 가정하겠다.
arrNum = np.array([7, 5, 1, 4, 6, 3, 2], int)

# 출력을 위한 변수 ----- START
arrResult = np.array([], int)
firstPivot = len(arrNum) // 2
cnt = 0
# -------------------- END

def sortQuick(arr):
    global arrResult
    
    # 
    if len(arr) <= 1:
        return arr
    
    # 빈배열 정의_[작은값] [중앙값][큰값]
    arrLess = np.array([], int)
    arrEqual = np.array([], int)
    arrGreat = np.array([], int)
    
    # 연산자// : 나누기한 값을 정수로 가져오기(소숫점버림)
    pivot = arr[len(arr) // 2]
    
    for n in arr:
        if n < pivot:
            arrLess = np.append(arrLess, n)
            # print("arrLess: {}" .format(n))
        elif n > pivot:
            arrGreat = np.append(arrGreat, n)
            # print("arrGreat: {}" .format(n))
        else:
            arrEqual = np.append(arrEqual, n)
            # print("arrEqual: {}" .format(n))

    print("-----")
    print("리턴값 {} - {} - {}" .format(arrLess, arrEqual, arrGreat))
    
    global cnt
    if cnt < firstPivot:
        arrResult = np.insert(arrResult, 0, arrEqual)
        cnt += 1    
    else:
        arrResult = np.append(arrResult, pivot)
    
    if len(arrLess) == 1 :
        arrResult = np.insert(arrResult, 0, arrLess)
        print(arrEqual)
        print(arrLess)   
    elif len(arrGreat) == 1 :
        arrResult = np.append(arrResult, arrGreat)
        print(arrEqual)
        print(arrGreat)
    else :
        print(arrEqual)
    
    return sortQuick(arrLess) + arrEqual + sortQuick(arrGreat)
    
    print(pivot)

#_____ 출력
print("기본데이터: {}" .format(arrNum))
print("===============================")
sortQuick(arrNum)
print("===============================")
print("퀵정렬 수행결과\n{}" .format(arrResult))