n = 600851475143
res = []
if(n%2==0):
    res.append(2)
while n%2==0:
    maxPrime =2
    n/=2

for i in range(3,int(n**(1/2)),2):
    if(n%i==0):
        res.append(i)
        n/=i
print(res)

