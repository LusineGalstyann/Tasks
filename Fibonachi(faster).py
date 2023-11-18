def fib(n, memo={}):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

result = fib(10)
print(result)

# def fib(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#
#     a, b = 0, 1
#     for _ in range(3, n+1):
#         a, b = b, a + b
#
#     return b
