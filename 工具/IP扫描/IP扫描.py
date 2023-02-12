import os     #OS模块可以调用电脑终端
for i in range(1,256):
    for x in range(1,256):
        wang=os.popen("fping -c 1 -t 1 172.16."+str(i)+"."+str(x)).readlines()     #第一个括号是执行的命令，IP可以更改。第二个是读取数据
        ze=str(wang).find("bytes")
        if ze>=0:     #判断是否发送成功
            data=open("/root/123.txt","a")     #在路径下创建文件夹
            print("172.16."+str(i)+"."+str(x)+"\n login OK",file=data)     #将扫描结果写入
            data.close()
else:
            print("172.16."+str(i)+"."+str(x)+"\n login down")
