#find the smallest number that is divisible by all numbers between 1 to 10
x = [i*7 for i in range(1,1000000)]

for i in x:
    if i%2==0 and i%3==0 and i%4==0 and i%5==0 and i%6==0 and i%7==0 and i%8==0 and i%9==0 and i%10==0:
        print(i)
        break
