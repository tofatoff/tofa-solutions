vowels = ['A','U','E','O','I']
consonants = "JSBKTCLDMVNWFXGPYHQZR"
v = []
c = []

for i in range(5):
    for j in range(21):
        v.append(vowels[i])

for i in range(21):
    for j in range(5):
        c.append(consonants[i])

N = int(input())

for i in range(N):
    name = []
    vow = []
    con = []
    n = int(input())

    if n % 2 == 1:
        for j in range(int((n+1)/2)):
            vow.append(v[j])
    else:
        for j in range(int(n/2)):
            vow.append(v[j])

    for j in range(int((n/2))):
        con.append(c[j])

    vow = sorted(vow)
    con = sorted(con)

    for k in range(len(vow)):
        name.append(vow[k])
        if k < len(con):
            name.append(con[k])

    name = ''.join(name)

    print("Case "+str(i+1)+":",name)