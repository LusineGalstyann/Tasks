"""
Take 2 strings s1 and s2 including only letters from a to z.
Return a new sorted string (alphabetical ascending), the longest possible,
containing distinct letters - each taken only once - coming from s1 or s2.

"""


def longest(a1, a2):
    s=sorted(set(a1 + a2))
    result=""
    for i in s:
        result+=i
    return result


print(longest("bca", "xxdad"))
