def digital_root(n):
    root = n
    while root > 9:
        digits = []
        n = root
        while n >= 1:
            digits.append(int(n % 10))
            n = n // 10
            print(digits, n)
        root = sum(digits)
        print("root " + str(root))

    return root


print(digital_root(397))

# 123 3=n%10 123-3
