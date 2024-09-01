# input is a string of three chars from the set 'D', 'F', 'I', 'K';
# output is a single char from this set
def trilingual_democracy(group):
    f, s, t = group[0], group[1], group[2]
    langs = ['D', 'F', 'I', 'K']
    if f == s and s == t:
        return group[0]
    elif f != s and f != t and s != t:
        for i in group:
            langs.remove(i)
        return langs[0]
    else:
        for i in group:
            if group.count(i) == 1:
                return i


print(trilingual_democracy("FFF"))
print(trilingual_democracy("IIK"))
print(trilingual_democracy("DFK"))
