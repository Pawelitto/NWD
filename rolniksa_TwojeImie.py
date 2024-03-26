# Funkcja obliczająca największy wspólny dzielnik (NWD) dwóch liczb
def znajdz_nwd(a, b):
    while b != 0:  
        a, b = b, a % b
    return a  

# Funkcja obliczająca największy wspólny dzielnik dla czterech liczb
def policz_paczki(a, b, c, d):
    nwd_ab = znajdz_nwd(a, b)
    nwd_cd = znajdz_nwd(c, d)
    nwd = znajdz_nwd(nwd_ab, nwd_cd)
    
    return nwd

rzodkiewka = 420
pietruszka = 300
cebula = 180
seler = 120

# Wywołanie Funkcji głównej
nwd = policz_paczki(rzodkiewka, pietruszka, cebula, seler)

# Wyświetlanie wyniku
print('Liczba paczek włoszczyzny to: {0}'.format(nwd))
