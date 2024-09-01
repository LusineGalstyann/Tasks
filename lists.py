
N = int(input())
l = []
for _ in range(N):
    values = input().split(" ")
    print(values, values[0])

    match values[0]:
        case "insert":
            l.insert(int(values[2]), int(values[1]))
        case "print":
            print(l)
        case "remove":
            l.remove(int(values[1]))
        case "append":
            l.append(int(values[1]))
        case "sort":
            l.sort()
        case "pop":
            l.pop()
        case "reverse":
            l[::-1]
        case _:
            print("You do not have any access to the code")

print("list is:"+str(l))

