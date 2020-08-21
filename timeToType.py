keys = 'abcdefghijklmnopqrstuvwxyz'
given = 'cba'
dic = {}
i = 0
for j in keys:
    dic[j] = i
    i+=1
count = 0
init ='a'
for i in given:
    count+=abs(dic.get(i)-dic.get(init))
    init = i
print(count)