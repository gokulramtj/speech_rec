import time
from datetime import datetime

f = open("project_log.txt", "a+")
flag = True
while(flag):
    ip = input()
    if(ip==""):
        flag = False
    else:
        tstamp = str(datetime.fromtimestamp(time.time()))
        f.write(tstamp + "\t" + ip + "\n")  

f.close()