import socket
import threading
import os
x = []
g = input('which ip you want(ip v4): ') 
if len(g) > 1:
    pass
else:
     exit()
try:
    m = input('port 0-?(default 0-3000 or all for 65535 port): ')
    if m == 'all':
        m = 65535
except:
    m = 3000
def a(port, g):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0) 
            s.settimeout(0.5)
            s.connect((g,port))
            print(port,' is open')
            x.append(port)
        except:
            pass
try:
    for i in range(1,int(m)):
        l = threading.Thread(target=a,args=(i,g))
        l.start()
except:
    for i in range(1,3000):
        l = threading.Thread(target=a,args=(i,g))
        l.start()
r = input('want nmap for more sure serve?(y/n)')
l = ''
if(r == 'y'):
    for i in x:
        l = l + str(i) + ','    
    os.system('nmap '+ g +' -sV -p '+l)
else: 
     print(x)
