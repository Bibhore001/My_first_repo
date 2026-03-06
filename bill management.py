import mysql.connector
import sys
while True:
    print("*_*_*_*_MENU_*_*_*")
    print("1- CREATE DATABASE \n2- SHOW DATABASE\n3- CREATE TABLE\n4-SHOW TABLES")
    print("5- DESC TABLE\n6- INSERT DATA\n7- DISPLAY\n8- UPDATE DATA")
    print("9- DELETE DATA\n 10- SEARCH \n 11- EXIT")
    ch=int(input("enter your choice"))
    if ch==1:
        mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123")
        mycursor=mydb.cursor()
        mycursor.execute("create database if not exists bibhore")
        print("database created")
    if ch==2:
        mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123")
        mycursor=mydb.cursor()
        mycursor.execute("show databases")
        for i in mycursor:
            print(i)
    if ch==3:
        mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
        mycursor=mydb.cursor()
        mycursor.execute("create table if not exists bill (PID integer(4) primary key,PNAME varchar(20) not null,PRICE integer(8) not null,DISCOUNT integer(3) not null,QUANTITY integer(8) not null,INSTOCK integer(8) not null,SOLDOUT integer(8) not null)")
        print("table created")
    if ch==4:
        mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
        mycursor=mydb.cursor()
        mycursor.execute("show tables")
        for i in mycursor:
            print(i)
    if ch==5:
        mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
        mycursor=mydb.cursor()
        mycursor.execute('desc bill')
        for i in mycursor:
            print(i)
    if ch==6:
        mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
        mycursor=mydb.cursor()
        n=int(input('HOW MANY RECORDS  YOU WANT TO ENTER?'))
        for i in range(n):
            pid=int(input('enter product id: '))
            pna=input('enter product name: ')
            pri=int(input('enter price: '))
            d=int(input('enter discounted price: '))
            q=int(input('enter quantity: '))
            inst=int(input('enter in stock quantity: '))
            sold=int(input('enter sold out quantity: '))
            query=("insert into bill values({},'{}',{},{},{},{},{})".format(pid,pna,pri,d,q,inst,sold))
            mycursor.execute(query)
            mydb.commit()
    if ch==7:
         mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
         mycursor=mydb.cursor()
         mycursor.execute('select * from bill ')
         for i  in mycursor:
             print("pid,pname,price,dicount,quantity,instock,soldout")
             print(i)
    if ch==8:
        mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
        mycursor=mydb.cursor()
        while True:
            print('MENU')
            print('1.pid \n 2.pname \n 3.price \n 4.quantity \n 5.in stock \n 6.sold out \n 7.exit')
            ch=int(input('enter choice: '))
            if ch==1:
                q=int(input('enter the id you want to  update'))
                r=int(input('enter the new value: '))
                mycursor.execute('update bill set PID={} where PID={}'.format(r,q))
                print('data updated')
                mydb.commit()
            if ch==2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
                mycursor=mydb.cursor()
                n=input('enter pname you want  to update: ')
                n2=input('enter new pname: ')
                mycursor.execute("update bill set PNAME='{}' where Pname='{}' ".format(n2,n))
                print('data updated')
                mydb.commit()
            if ch==3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
                mycursor=mydb.cursor()
                n=input('enter price you want  to update: ')
                n2=input('enter new price: ')
                mycursor.execute("update bill set PRICE={} where PRICE={} ".format(n2,n))
                print('data updated')
                mydb.commit()
            if ch==4:
                mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
                mycursor=mydb.cursor()
                n=input('enter quantity you want  to update: ')
                n2=input('enter new quantity: ')
                mycursor.execute("update bill set QUANTITY={} where QUANTITY={} ".format(n2,n))
                print('data updated')
                mydb.commit()
            if ch==5:
                mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
                mycursor=mydb.cursor()
                n=input('enter in stock you want  to update: ')
                n2=input('enter new in stock: ')
                mycursor.execute("update bill set INSTOCK={} where INSTOCK={} ".format(n2,n))
                print('data updated')
                mydb.commit()
            if ch==6:
                mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
                mycursor=mydb.cursor()
                n=input('enter in sold out want  to update: ')
                n2=input('enter new sold out: ')
                mycursor.execute("update bill set SOLDOUT={} where SOLDOUT={} ".format(n2,n))
                print('data updated')
                mydb.commit()
            if ch==7:
                break
    if ch==9:
         mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
         mycursor=mydb.cursor()
         s=int(input('enter pid you want to delete: '))
         mycursor.execute('delete from bill where PID={}'.format(s))
         print('record deleted')
         mydb.commit()
    if ch==10:
        mydb=mysql.connector.connect(host="localhost",user="root",password="bibhore123",database="bibhore")
        mycursor=mydb.cursor()
        s=int(input('enter pid you want to search: '))
        mycursor.execute('select * from bill where PID={}'.format(s))
        for i  in mycursor:
             print("pid,pname,price,dicount,quantity,instock,soldout")
             print(i)
        mydb.commit()
    if ch==11:
        sys.exit()
