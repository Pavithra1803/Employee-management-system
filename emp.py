import sqlite3
con=sqlite3.connect("c:\sqlite3\Second.db")
cur=con.cursor()
class Employee:
    cur.execute("create table if not exists Employee(id integer primary key,fname text(50),lname text(50),sal integer,designation text(50),phn integer)")
    def join(self,id,fname,lname,sal,designation,phn):
        cur.execute("insert into Employee values(?,?,?,?,?,?)",(id,fname,lname,sal,designation,phn))
        con.commit()
        print("Employee details entered successfully")
    def view(self,id):
        cur.execute(f"select * from Employee where id={id}")
        i=cur.fetchall()
        if not i:
            print("no such employee")
        else:
            print(i)
    def update(self,id,col,newdata):
        cur.execute(f"select id from Employee where id={id}")
        i = cur.fetchone()
        if i:
            cur.execute(f"update Employee set {col}={newdata} where id={id}")
            print("Details updated successfully")
        else:
            print("no such user")
    def remove(self,id):
        cur.execute(f"select id from Employee where id={id}")
        i=cur.fetchall()
        if not i:
            print("no such employee")
        else:
            cur.execute(f"delete from Employee where id={id}")
            print("employee removed successfully")
obj=Employee()
print("Employee Management System\n")
exit=1
while(exit):
    print("1.Joining")
    print("2.view details")
    print("3.update details")
    print("4.Remove Employee")
    s=int(input("\nenter your option"))
    match(s):
        case 1:
            id=int(input("enter id"))
            fname=input("enter first name")
            lname=input("enter last name")
            sal=int(input("enter salary"))
            designation=input("enter designation")
            phn=int(input("enter mobile number"))
            obj.join(id,fname,lname,sal,designation,phn)
        case 2:
            id = int(input("enter id"))
            obj.view(id)
        case 3:
            id = int(input("enter id"))
            col= input("enter column to be updated")
            newdata= int(input("enter new data"))
            obj.update(id,col,newdata)
            con.commit()
        case 4:
            id = int(input("enter id"))
            obj.remove(id)
            con.commit()
    exit=int(input("enter 0 for exit,1 for continue"))
print("\n---------Thankyou---------")