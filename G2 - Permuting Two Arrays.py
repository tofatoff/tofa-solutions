q = int(input())

permuting = True

for i in range(q):
    nk = input()
    n,k = map(int,nk.split())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A = sorted(A)
    B.sort(reverse=True)

    for j in range(n):
        if A[j] + B[j] < k:
            permuting = False

    if permuting:
        print("YES")
    else:
        print("NO")