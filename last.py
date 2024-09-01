def last(*a):
    box = a[-1]
    if isinstance(box, (list, str)) and len(a) == 1:
        return box[-1]
    else:
        return (box)


print(last(5))
print(last([1, 2, 3, 4]))
print(last("xyz"))
print(last(1, 2, 3, 4))
print(last([1, 2], [3, 4]))
print(last([[1, 2], [3, 4]]))
