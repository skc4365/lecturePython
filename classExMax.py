
import numpy as np

# 입력횟수
cnt = 5;

# 빈 배열 _____ dtype = np.int64설정.
arrNum = np.array([], dtype = np.int64)
# arrNum = np.array([], dtype = "i")

# 입력함수
def valInput(v):
    global arrNum
    arrNum = np.append(arrNum, v)
    
# 입력구문
for i in range(cnt):
    valInput(int(input("0~99의 숫자를 입력하세요: ")))
# =============================================================================    


# 출력구문 TYPE111
valMax = 0
indexMax = 0
i = 0

while i < len(arrNum):
    if arrNum[i] > valMax : valMax = arrNum[i]; indexMax = i
    i += 1
    
print("가장큰값: " + str(valMax) + "이고, 위치는: " + str(indexMax))



# =============================================================================
# # 출력구문 TYPE222
# # _____ 최대값 np.max()
# valMax = np.max(arrNum)
# # _____ 인덱스(위치값) np.where()
# indexMax = np.where(valMax == arrNum)
# 
# # 출력 _____ 문자열의 나열
# print("최대입력값은: " + str(valMax) + "인덱스값: " + str(indexMax))  
# 
# # 출력 _____ .format()
# print("최대값 {}의 인덱스값은 {}이다 " .format(valMax, indexMax[0]))
# 
# =============================================================================


