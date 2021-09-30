import numpy as np

#===== 버블정렬 =====
arrNum = np.array([57, 33, 41, 91, 7, 18, 52, 23], int)

def sortBubble():
        
    for i in range(len(arrNum) - 1, 0, -1):
        # print(i)
        for j in range(i):
            if arrNum[j] > arrNum[j + 1]:
                arrNum[j], arrNum[j + 1] = arrNum[j + 1], arrNum[j]
        print("{}번째: {}" .format(i, arrNum))

#_____ 출력
print("기본데이터: {}" .format(arrNum))
print("===============================")
sortBubble()
print("===============================")
print("버블정렬 수행결과\n{}" .format(arrNum))