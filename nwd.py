import math

def znajdz_pare_z_najwiekszym_nwd(a, b, c):
    nwd_ab = math.gcd(a, b)
    nwd_bc = math.gcd(b, c)
    nwd_ac = math.gcd(a, c)

    if nwd_ab == nwd_bc == nwd_ac:
        print("Pary mają taki sam NWD")
    else:
        maks_nwd = max(nwd_ab, nwd_bc, nwd_ac)
        if maks_nwd == nwd_ab:
            print(f"{a} i {b}")
        elif maks_nwd == nwd_bc:
            print(f"{b} i {c}")
        else:
            print(f"{a} i {c}")

znajdz_pare_z_najwiekszym_nwd(7, 100, 150)
