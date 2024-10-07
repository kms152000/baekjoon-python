#첫째 줄에는 현재 시각이 나온다. 
# 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.
H, M = input().split()
H = int(H)
M = int(M)
U = int(input())

if(M + U >= 60):
    if((H+int((M+U)/60))>=24):
        print((H+int((M+U)/60))-24, (M+U)%60)
    else:
        print((H+int((M+U)/60)), (M+U)%60)
else:
    print(H, M+U)

