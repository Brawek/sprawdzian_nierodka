def algorytm_cyfry(n):
    c = 0
    b = 1
    licznik_dodawan = 0
    
    temp_n = n
    while temp_n > 0:
        a = temp_n % 10
        if a % 2 == 0:
            c = c + (a // 2) * b
        else:
            c = c + b
            licznik_dodawan += 1
        
        b = b * 10
        temp_n = temp_n // 10
        
    return c, licznik_dodawan


n1 = 542102
n2 = 87654321012345678

wynik1, dodawania1 = algorytm_cyfry(n1)
wynik2, dodawania2 = algorytm_cyfry(n2)

print(f"n={n1} -> c={wynik1}, dodawania={dodawania1}")
print(f"n={n2} -> c={wynik2}, dodawania={dodawania2}")