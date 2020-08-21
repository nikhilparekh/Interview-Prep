a = [2,4,5,1,2]
def water(A,cap1,cap2):
    cur_cap1 = cap1
    cur_cap2 = cap2
    count = 0
    i =0
    j = len(a)-1
    while(i<=j):
        if(a[i]>cur_cap1):
            count+=1
            cur_cap1 = cap1
        else:
            cur_cap1-=a[i]
            i+=1
            # print(cap1)
        if(a[j]>cur_cap2):
            count+=1
            cur_cap2 = cap2
        else:
            cur_cap2-=a[j]
            j-=1
        
        
    print(count)

water(a,5,7)
