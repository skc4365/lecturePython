import numpy as np

#===== 선택정렬 =====
arrNum = np.array([57, 33, 41, 91, 7, 18, 52, 23], int)

def sortSelection_Min():
        
    for i in range(len(arrNum)-1):
        minIdx = i
        # print(minIdx)
        for j in range(i+1, len(arrNum)):
            if arrNum[minIdx] > arrNum[j]:
                minIdx = j
        arrNum[i], arrNum[minIdx] = arrNum[minIdx], arrNum[i]
        print("{}번째: {}" .format(i, arrNum))

#_____ 출력
print("기본데이터: {}" .format(arrNum))
print("===============================")
sortSelection_Min()
print("===============================")
print("선택정렬 수행결과\n{}" .format(arrNum))