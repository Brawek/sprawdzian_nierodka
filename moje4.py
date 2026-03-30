plik = open('../liczby.txt', 'r')
wiersze = plik.readlines()

pierwsze_string = wiersze[0].strip().split(' ')
calkowite_string = wiersze[1].strip().split(' ')

pierwsze = []
calkowite = []

for pierwsza in pierwsze_string:
    pierwsze.append(int(pierwsza)) 
for calkowita in calkowite_string:
    calkowite.append(int(calkowita))


#1.
ile = 0
for pierwsza in pierwsze:
    for calkowita in calkowite:
        if calkowita % pierwsza == 0:
            ile+=1
            break
print(ile)     

#2.
sorted_ = sorted(pierwsze, reverse=True)
print(sorted_[100])

#3.
def rozklad(n):
    czynniki = []
    i = 2

    while i * i >= n:
        while n % i == 0:
            czynniki.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        czynniki.append(n)
    return czynniki

for calkowita in calkowite:
    czynniki = rozklad(calkowita)
    pierwsze_copy = pierwsze.copy()
    gotit = True
    for czynnik in czynniki:
        if czynnik not in pierwsze_copy:
            gotit = False
            break
        else:
            pierwsze_copy.remove(czynnik)
    if gotit:
        print(calkowita)


#4.
max_srednia = 0
max_count = 50
max_begin = -1

for rozmiar_okna in (50, len(pierwsze) + 1):
    suma = sum(pierwsze[:rozmiar_okna])
    srednia = suma / rozmiar_okna
    if srednia > max_srednia:
        max_srednia = srednia
        max_count = rozmiar_okna
        max_begin = 0

    for i in (rozmiar_okna, len(pierwsze)):
        suma = suma - rozmiar_okna[i] + pierwsze[i - rozmiar_okna]
        srednia = suma / rozmiar_okna
        if srednia > max_srednia:
            max_srednia = srednia
            max_count = rozmiar_okna
            max_begin = i - rozmiar_okna + 1

print(max_begin, max_count, max_srednia)