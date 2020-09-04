totalShare = 3
bids = [[1,2,5,0],[2,1,4,2],[3,5,4,6]]

#id #n-shares #price #time

bids = sorted(bids,key=lambda x:x[2],reverse = True)
got = set()
for i in range(1,len(bids)):
    for j in range(i):
        if totalShare:
            if bids[i-1][2]>bids[i][2]:
                totalShare-=bids[i-1][1]
                got.add(bids[i-1][0])
            elif bids[i-1][2]==bids[i][2]:
                if bids[i-1][3]<bids[i][3]:
                    totalShare-=1
                    got.add(bids[i-1][0])
                    if totalShare:
                        totalShare-=1
                        got.add(bids[i][0])
                else:
                    totalShare-=1
                    got.add(bids[i][0])
                    if totalShare:
                        totalShare-=1
                        got.add(bids[i-1][0])
        else:
            break


for i in range(1,len(bids)+1):
    if i not in got:
        print(i)
                
        


