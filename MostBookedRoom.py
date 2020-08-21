a = ["+3E", "-1A", "+4F", "+1A", "-3E", "+1A","+1A","+1A","+1A","+1A", "+3E", "+3E","+3E","+3E","+3E","+3E"]
times = {}
for i in a:
    times[i] = a.count(i)
# times = sorted(times)
print(times)
x = {k:v for k,v in sorted(times.items(), key=lambda kv : kv[1],reverse=True)}
li = list(x.keys())
print(li[0])