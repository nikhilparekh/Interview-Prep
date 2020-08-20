a ='nikhil'
# a = a.replace('i','z')
for i in a:
    if(i=='i'):
        a = a.replace(i,'z',1)
        break
print(a)