if __name__ == '__main__':

    nested_list = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])

    new_list = sorted(nested_list, key=lambda x: x[1])
    min = new_list[0][1]

    names = []
    start = 0
    for i, j in new_list[1:]:
        if j > min and start == 0:
            names.append(i)
            start = j
            continue
        if start == j and start != 0:
            names.append(i)

    for i in sorted(names):
        print(i)




