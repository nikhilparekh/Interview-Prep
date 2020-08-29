time = "1?:?2"

if time[0] == "?":
    if time[1] == "?":
        ans = '2'
        time = time.replace('?',ans)
        # time = time.replace('?','3',1)
    elif int(time[1])>3:
        ans = '1'
        time = time.replace('?',ans)
    else:
        ans = '2'
        time = time.replace('?',ans)
elif time[1] == '?':
    if time[0] == '?':
        ans = '2'
        time = time.replace('?',ans)
        # time = time.replace('?','3',1)
    elif int(time[0])>1:
        ans = '3'
        time = time.replace('?',ans)
    else:
        ans = '9'
        time = time.replace('?',ans)
elif time[3] == "?":
    ans = '5'
    time = time.replace('?',ans)
elif time[4] == "?":
    ans = '9'
    time = time.replace('?',ans)

print(time)
