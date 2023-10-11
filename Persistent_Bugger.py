def persistence(n):
    if n < 10:
        return 0
    m = 1
    for i in str(n):
        m *= int(i)
    return 1 + persistence(m)


print(persistence(39))
