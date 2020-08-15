def addDigit(num):
    if(num<=0):
        return 0
    count = num%10
    num//=10
    return count+addDigit(num)

print(addDigit(4321))