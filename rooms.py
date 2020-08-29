a = ["+4B"]*600

s = set()

for i in a:
    if i.startswith('+'):
        s.add(i)
print(len(s))