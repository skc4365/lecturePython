import numpy as np

#===== 버블정렬 =====
arrNum = np.array([57, 33, 41, 91, 7, 18, 52, 23], int)

def sortInsertion():
        
    for i in range( 1, len(arrNum)):
        # print(i)
        for j in range(i, 0, -1):
            if arrNum[j-1] > arrNum[j]:
                # print(j)
                arrNum[j-1], arrNum[j] = arrNum[j], arrNum[j-1]
            # print("j:{}번째--- {}" .format(j, arrNum))
        print("{}번째: {}" .format(i, arrNum))

#_____ 출력
print("기본데이터: {}" .format(arrNum))
print("===============================")
sortInsertion()
print("===============================")
print("삽입정렬 수행결과\n{}" .format(arrNum))