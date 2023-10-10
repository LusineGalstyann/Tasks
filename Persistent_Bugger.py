def persistence(n):
    digit = []
    step = 0
    while n > 10:
        digit.append(n % 10)
        n = n // 10
    digit.append(n)
    mul = 1
    while mul > 10 or step==0:
        for i in digit:
            print(i)
            mul *= i
            step += 1
    print(mul)
    print(step)


persistence(144)
