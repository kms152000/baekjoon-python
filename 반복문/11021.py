T = int(input())

for i in range(1, T+1):
	A, B = input().split()
	A = int(A)
	B = int(B)
	sum = A+B
	print(f'Case #{i}: {sum}')
