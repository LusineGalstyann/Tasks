import re

s = input()
k = input()

pattern = re.compile(k)
x = pattern.search(s)
if not x: print('(-1, -1)')
while x:
    print('({0}, {1})'.format(x.start(), x.end() - 1))
    x = pattern.search(s, x.start() + 1)