'''
Hotel Management System

Soumyajit Kolay and Ankit Roy (c) All Rights Reserved.
'''
import mysql.connector as dbsys
import datetime
import os
os.system("cls")
psswd=input("Enter MySQL Database Password:\n ?:\t")
print("Attempting to Connect to Database, Please Stand By!")
print("")



hmsdb=dbsys.connect(host="localhost",user="root",passwd=psswd,database="hms")
cr=hmsdb.cursor()

for i in range(0,500):
    pass
os.system("cls")

def tariff():
    print("____________________________")
    print("|1.  Deluxe AC @INR2500/Day|")
    print("|2.  Deluxe    @INR2000/Day|")
    print("|3.  AC        @INR1800/Day|")
    print("|4.  Non-AC    @INR1200/Day|")
    print("|__________________________|")

def checknew():
    rt=int(input("Room Type:\t[DAC:1,DN:2,AC:3,N:4]"))
    print("Checking...")
    if rt==1:
        cr.execute("select rno from rooms where (rtype='DAC' and cname='');")
        x=cr.fetchall()
    elif rt==2:
        cr.execute("select rno from rooms where (rtype='DN' and cname='');")
        x=cr.fetchall()
    elif rt==3:
        cr.execute("select rno from rooms where (rtype='AC' and cname='');")
        x=cr.fetchall()
    elif rt==4:
        cr.execute("select rno from rooms where (rtype='N' and cname='');")
        x=cr.fetchall()
    print("Found Results:")
    for i in x:
        print(i)
    return

def newcust():
    rno=int(input("Input Room No."))
    rnos=str(rno)
    cname=input("Enter Customer Name:")
    custnum=int(input("Enter number of members:"))
    cns=str(custnum)
    entrydts=datetime.date.today()
    entrydt=str(entrydts)
    daysno=int(input("Number of days:"))
    exitdts=entrydts+datetime.timedelta(days=daysno)
    exitdt=str(exitdts)
    phno=input("PHNO:")
    execstr="UPDATE rooms set cname='"+cname+"', custnum="+cns+", entrydt='"+entrydt+"', exitdt='"+exitdt+"', phno='"+phno+"' where rno="+rnos+";"
    cr.execute(execstr)
    hmsdb.commit()
    return

def checkouts():
    dtchk=str(datetime.date.today())
    cr.execute("select * from rooms where exitdt='"+dtchk+"';")
    x=cr.fetchall()
    print("Rooms to Be checked out today:")
    for i in x:
        print("Room No.     ",i[0])
        print("Room Type    ",i[1])
        print("Customer Name",i[2])
        print("People(s)    ",i[3])
        print("Date From/To ",i[4],"to",i[5])
        print("Room Type    ",i[6])
    return

def chkroomout():
    rno=int(input("Enter Room Number:\t"))
    rnos=str(rno)
    cr.execute("select * from rooms where rno="+rnos+";")
    x=cr.fetchone()
    print(x)
    tempinp=input("Press Y and enter to confirm:")
    if tempinp=='Y':
        exitdts=x[5]
        enterdts=x[4]
        days=int((exitdts-enterdts).days)
        fees=0
        if x[1]=='DAC':
            fees=2500*days+100*x[3]
        elif x[1]=='DN':
            fees=2000*days+100*x[3]
        elif x[1]=='AC':
            fees=1800*days+100*x[3]
        elif x[1]=='N':
            fees=1200*days+100*x[3]
        print("Thank You\n Days="+str(days)+"\n Fees="+str(fees))
        cr.execute("UPDATE rooms set cname='', custnum=0, entrydt='1970-01-01', exitdt='1970-01-01', phno='0' where rno="+rnos+";")
        hmsdb.commit()
    return


def roomqry():
    rno=int(input("Enter Room No."))
    rnos=str(rno)
    cr.execute("select * from rooms  where rno="+rnos+";")
    x=cr.fetchone()
    print("Room No.     ",x[0])
    print("Room Type    ",x[1])
    print("Customer Name",x[2])
    print("People(s)    ",x[3])
    print("Date From/To ",x[4],"to",x[5])
    print("Room Type    ",x[6])

'''
rno integer, rtype char(4), cname char(40), custnum integer,
entrydt date, exitdt date, phno char(10), primary key (rno)
___________________________________________________________
0   1       2       3       4       5       6
rno rtype   cname   custnum entrydt exitdt  phno
___________________________________________________________
'''

def roomcrt():
    rno=int(input("Input a no."))
    rnos=str(rno)
    rtype=input("Room Type Abbr.[DAC/DN/AC/N]:")
    cr.execute("insert into rooms values("+rnos+",'"+rtype+"','',0,'1970-01-01','1970-01-01','0'"+");")
    hmsdb.commit()
    return

def menu():
    print("________________________________")
    print("|Welcome To HMS Comsole        |")
    print("|1.  Tariff                    |")
    print("|2.  New Customer/Update Entry |")
    print("|3.  Check for Checkouts       |")
    print("|4.  Check Room Out            |")
    print("|5.  Query Room Info           |")
    print("|6.  Register New Room         |")
    print("|7.  Quit                      |")
    print("|______________________________|")

menu()
while True:

    x=input("?:\t")
    if int(x)==1:
        tariff()
        input("Press Enter")
        os.system("cls")
        menu()
    if int(x)==2:
        checknew()
        newcust()
        input("Press Enter")
        os.system("cls")
        menu()
    if int(x)==3:
        checkouts()
        input("Press Enter")
        os.system("cls")
        menu()
    if int(x)==4:
        chkroomout()
        input("Press Enter")
        os.system("cls")
        menu()
    if int(x)==5:
        roomqry()
        input("Press Enter")
        os.system("cls")
        menu()
    if int(x)==6:
        roomcrt()
        input("Press Enter")
        os.system("cls")
        menu()
    if int(x)==7:
        break
#--------------------------ENDS----------HERE-------------------------------------------
