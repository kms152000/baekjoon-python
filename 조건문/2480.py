'''
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
'''
d1, d2, d3 = input().split()
d1 = int(d1)
d2 = int(d2)
d3 = int(d3)

if(d1 == d2 == d3):
    print(10000 + d1*1000)
elif(d1 == d2 or d1 == d3):
    print(1000 + d1*100)
elif(d2==d3):
    print(1000 + d2*100)
else:
    if(d1 > d2 and d1 > d3):
        print(d1*100)
    elif(d2 > d3):
        print(d2*100)
    else:
        print(d3*100)