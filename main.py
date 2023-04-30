N = 5
A = [4, 8, 2, 1, 3]

MIN = 2
MAX = 4

for i in range(N):
    if MIN <= A[i] <= MAX:
        print(i, end = ' ')