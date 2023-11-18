def sortme(words):
    return sorted(words, key=str.lower)


print(sortme(["Hello", "there", "I'm", "fine"]))
print(sortme(["C", "d", "a", "B"]) )
