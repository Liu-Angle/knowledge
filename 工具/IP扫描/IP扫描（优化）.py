import os
for i in range(1,256):
    for x in range(1,256):
        A=os.popen("fping -c 1 -t 1 192.168."+str(i)+"."+str(x)).readlines()
        B=str(A).find("bytes")
        if B>=0:
            data=open("IP扫描结果.txt","a")
            print("后两位为："+str(i)+"."+str(x)+" 的主机开放",file=data)
            data.close() 
