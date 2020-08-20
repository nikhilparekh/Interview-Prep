time = "??:??"

if time[0] == "?":
    if time[1] == "?":
        time = time.replace('?','2',1)
        time = time.replace('?','3',1)
    elif int(time[1])>3:
        time = time.replace("?","1",1)
    else:
        time = time.replace("?","2",1)
if time[1] == '?':
    if time[0] == '?':
        time = time.replace('?','2',1)
        time = time.replace('?','3',1)
    elif int(time[0])>1:
        time = time.replace("?","3",1)
    else:
        time = time.replace("?","9",1)
if time[3] == "?":
    time = time.replace("?","5",1)
if time[4] == "?":
    time = time.replace("?","9",1)

print(time)
