a = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]

di ={}

for i in a:
    di[i] = a.count(i)
summ = 0
drop = 0
for i in di:
    summ+=di[i]
    if di[i]>3:
        drop+=di[i]-3