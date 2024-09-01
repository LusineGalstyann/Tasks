def solution(s):
    split_s=[]
    if len(s) % 2 == 1:
        s += '_'
    for i in range(0, len(s),2):
        split_s.append(s[i]+s[i+1])
    print(split_s)


solution("abc")
solution("abcdef")
