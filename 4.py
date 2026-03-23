import math

f = open('liczby.txt')
w1 = [int(x) for x in f.readline().split()]
w2 = [int(x) for x in f.readline().split()]

#4.1
odp41 = 0
for p in w1:
    for d in w2:
        if d % p == 0:
            odp41 += 1
            break
print(f"4.1: {odp41}")

#4.2
w1_sorted = sorted(w1, reverse=True)
print(f"4.2: {w1_sorted[100]}")

#4.3
def czy_mozna_zlozyc(n, magazyn):
    temp = n
    d = 2
    kopia_magazynu = magazyn.copy()
    while d * d <= temp:
        while temp % d == 0:
            if d not in kopia_magazynu or kopia_magazynu[d] <= 0:
                return False
            kopia_magazynu[d] -= 1
            temp //= d
        d += 1
    if temp > 1:
        if temp not in kopia_magazynu or kopia_magazynu[temp] <= 0:
            return False
    return True

magazyn = {}
for x in w1:
    magazyn[x] = magazyn.get(x, 0) + 1

odp43 = [n for n in w2 if czy_mozna_zlozyc(n, magazyn)]
print(f"4.3: {' '.join(map(str, odp43))}")

#4.4
max_s, naj_dl, naj_pierw = 0, 0, 0
for dl in range(50, len(w1) + 1):
    suma = sum(w1[:dl])
    for i in range(len(w1) - dl + 1):
        if i > 0:
            suma = suma - w1[i-1] + w1[i+dl-1]
        srednia = suma / dl
        if srednia > max_s:
            max_s, naj_dl, naj_pierw = srednia, dl, w1[i]

print(f"4.4: {max_s} {naj_dl} {naj_pierw}")