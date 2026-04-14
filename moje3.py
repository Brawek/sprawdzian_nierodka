plik = open('skrot.txt', 'r')
wiersze = plik.readlines()


#1
def nieparzysty_skrot(n):
    skrot = 0
    mnoznik = 1
    
    while n > 0:
        cyfra = n % 10 #7
        if cyfra % 2 == 1:
            skrot = skrot + cyfra * mnoznik
            mnoznik *= 10
        n //= 10
        
    return skrot

print(nieparzysty_skrot(39101))


#2
ile_nie_ma = 0
max_ktora_nie_ma = -1

for wiersz in wiersze:
    liczba = wiersz.strip()
    czy_moze_miec_skrot = False
    for cyfra in liczba:
        cyfra = int(cyfra)
        if cyfra % 2 == 1:
            czy_moze_miec_skrot = True
            
    if not czy_moze_miec_skrot:
        ile_nie_ma += 1
        liczba = int(liczba)
        if liczba > max_ktora_nie_ma:
            max_ktora_nie_ma = liczba

print(ile_nie_ma)
print(max_ktora_nie_ma)


#3
plik = open('skrot2.txt', 'r')
wiersze = plik.readlines()

for wiersz in wiersze:
    liczba = int(wiersz)
    liczba_skrot = nieparzysty_skrot(liczba)
    
    if math.gcd(liczba, liczba_skrot) == 7:
        print(liczba)