def nato(word):
    str=''
    dic=['Alpha', 'Bravo', 'Charlie','Delta','Echo','Foxtrot','Golf','Hotel','India','Juliett','Kilo','Limo','Mika','November','Oscar','Papa','Quebec','Romeo','Sierra','Tango','Uniform','Victor','Whishkey','Xray','Yankee','Zulu']
    for i in word.lower():
        str+=dic[ord(i)-97]+" "
    return(str)
    pass

print(nato('hi'))
print(nato('abc'))
print(nato('babbke'))
print(nato('banana'))