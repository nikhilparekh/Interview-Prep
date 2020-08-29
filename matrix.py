a = [[1,2],[3,4]]
# a = [[2,5],[7,17]]
b = [[0,0],[0,0]]
summ = 0
for i in range(len(a)):
    for j in range(len(a)):
        if i ==0 and j==0:
            b[i][j] == a[i][j]
        elif i==0 and j==1:
            b[i][j] = a[i][j]+b[0][0]
        elif i==1 and j==0:
            b[i][j] = a[i][j]+b[0][0]
        elif i==1 and j ==1:
            b[i][j] = b[0][0]+b[0][1]+b[1][0]+a[i][j]
        
print(b)