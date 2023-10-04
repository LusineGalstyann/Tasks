def nato(word):
    str=''
    dic=['Alpha', 'Bravo', 'Charlie','Delta','Echo','Foxtrot','Golf','Hotel','India','Juliett','Kilo','Lima','Mike','November','Oscar','Papa','Quebec','Romeo','Sierra','Tango','Uniform','Victor','Whiskey','X-ray','Yankee','Zulu']
    for i in word.lower():
        str+=dic[ord(i)-97]+" "
    return(str.rstrip())
    pass

print(nato('hi'))
print(nato('abc'))
print(nato('babbke'))
print(nato('banana'))