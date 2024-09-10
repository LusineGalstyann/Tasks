def a1_thick_and_hearty(a1, a2):
    same_val=[i for i in a1 for j in a2 if i==j]
    result= set()
    print(type(result))
    lists_lens=[len(a1),len(a2)]
    for i in range(len(same_val)):
        for j in range(i + 1, len(same_val)):
            if same_val[i]+same_val[j] in lists_lens or abs(same_val[i]-same_val[j]) in  lists_lens:
                result.update([same_val[i],same_val[j]])
    return result

print(a1_thick_and_hearty([1, 2, 3, 4, 5, 6],[1, 2, 4, 6, 7, 8, 9, 10])) #1,2,4,6