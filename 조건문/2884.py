#첫째 줄에 상근이가 창영이의 방법을 사용할 때, 설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)
H, M = input().split()
H = int(H)
M = int(M)

if(M <45):
    if(H == 0):
        print(H+23, M+15)
    else:
        print(H-1, M+15)
else:
    print(H, M-45)
    