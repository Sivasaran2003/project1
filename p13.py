msg =  [ (3, 2, 5, 'wait'),
(3, 0, 5, 'Time'),
(3, 1, 5, 'doesn’t'),
(3, 4, 5, 'anyone'),
(3, 3, 5, 'for'),
(1, 1, 2, 'Running'),
(1, 0, 2, 'keep') 
]
n = len(msg)
nt = len(msg[0])
m = 0
for i in range(0,n):
    m = i
    for j in range(i+1,nt):
        if msg[m][0] > msg[j][0] :
            m = j
        if msg[m][0] == msg[j][0] and msg[m][1] >= msg[j][1] :
            m = j
    #print(msg[m])
    temp = msg[i]
    msg[i] = msg[m]
    msg[m] = temp
print (msg)
        
