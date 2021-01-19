n = int(input())

work = 0

while n != 0:
    a = list(map(int,input().split()))

    for i in range(n-1):
        if a[i] < 0:
            work += a[i]*-1
        else:
            work += a[i] * 1

        a[i + 1] = a[i + 1] + a[i]
        a[i] = 0

    print(work)
    work = 0
    n = int(input())