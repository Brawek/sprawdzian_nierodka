import math

def wyznacz_skrot(n):
    m = 0
    waga = 1
    temp_n = n
    while temp_n > 0:
        cyfra = temp_n % 10
        if cyfra % 2 != 0: 
            m = cyfra * waga + m
            waga = waga * 10
        temp_n = temp_n // 10
    
    if m == 0 and waga == 1:
        return None
    return m

print("--3.1:")
n_ex = 294762
m_ex = wyznacz_skrot(n_ex)
print(f"Dla n={n_ex}, m={m_ex}, roznica n-m = {n_ex - m_ex}")

print("\n--3.2:")
liczby32 = [int(x) for x in open('skrot.txt')]
braki = [x for x in liczby32 if wyznacz_skrot(x) is None]
print(f"Liczba liczb bez skrotu: {len(braki)}")
print(f"Najwieksza z nich: {max(braki) if braki else 'Brak'}")

print("\n--3.3:")
print("Liczby n, gdzie NWD(n, m) == 7:")
for n in [int(x) for x in open('skrot2.txt')]:
    m = wyznacz_skrot(n)
    if m is not None:
        if math.gcd(n, m) == 7:
            print(n)