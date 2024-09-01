# it should return the continued fraction of de/nu in an array
def continued_fraction(nu: int, de: int) -> list[int]:
    des = []
    if nu == 0:
        return des
    a = nu // de
    b = nu - a * de
    d = de
    if b==0:
        return([a])
    while b !=0 :
        des.append(a)
        c = max(d, b)
        d = min(d, b)
        a = c // d
        b = c - a * d
    des.append(a)
    return des

print(continued_fraction(1089, 9))
print(continued_fraction(761, 327))
print(continued_fraction(1721, 9))

