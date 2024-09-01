def tail_swap(s):
    sp_1, sp_2 = s[0].split(":"), s[1].split(":")
    return [sp_1[0] + ":" + sp_2[1], sp_2[0] + ":" + sp_1[1]]


print(tail_swap(['abc:123', 'cde:456']))