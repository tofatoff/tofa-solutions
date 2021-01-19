n = int(input())

arr = list(map(int,input().split()))

arr = sorted(arr)

min = arr[0] - arr[1]

if (min < 0):
    min *= -1

for i in range(0,n-1):
    temp = arr[i] - arr[i+1]

    if temp < 0:
        temp *= -1
    if temp < min:
        min = temp

print(min)