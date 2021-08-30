
# Low_High 게임

import random

# 숫자의 영역(크기)설정
nMin = 1; nMax = 99; 
randomNum = random.randint(nMin, 99)

print(randomNum)
# 도전 횟수
cnt = 0

while True:
    selectNum = int(input("1~99예상되는 숫자를 입려하세요: "))
    cnt += 1
    
    if randomNum == selectNum:
        print("정답입니다: " + str(randomNum))
        break
    elif selectNum == 0:
        print("종료합니다.")
        break
    elif randomNum > selectNum:
        print("예상숫자보다 큰 값입니다.")
    elif randomNum < selectNum:
        print("예상숫자보다 작은 값입니다.")
    
    