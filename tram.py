n = int(input())
j = 0
k = 0
for i in range(n):
    a_i, b_i = map(int, input().split())
    j = j - a_i + b_i
    k = max(k, j)
print(k)
