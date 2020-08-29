T = '0?:??'

if T[0]=='?':
    hr='2'
    if T[1] =='?':
        hr='2'
        if T[3]=='?':
            hr='2'
            if T[4] == '?':
                hr = '2'
    elif int(T[1])>3:
        hr ='1'
elif T[1]=='?':
    if T[0]=='2':
        hr='3'
    elif T[0]=='1' and T[3]=='?':
        hr='5'
    else:
        hr='9'
elif T[3]=='?':
    hr='5'
else:
    hr='9'

T = T.replace('?',hr)
print(T)
