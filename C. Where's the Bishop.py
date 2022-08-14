for _ in range(int(input())):
	input()
	a = [input() for _ in range(8)]
	for i in range(1, 7):
		for j in range(1, 7):
			if a[i][j] + a[i - 1][j - 1] + a[i - 1][j + 1] == '###':
				print(f"{i + 1} {j + 1}")
				break
