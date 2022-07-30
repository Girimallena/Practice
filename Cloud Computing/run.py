from flask import Flask,render_template,request
import sqlite3

msg='vovlo'

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('log.html')




@app.route('/SIGNIN', methods=['POST','GET'])
def display():
    form1= request.form
    name =form1['uname']
    slot = form1['psw']
    u1=form1['typ']
    
    try: 
        con=sqlite3.connect('LOGIN.db')
        cur = con.cursor()
        pass1=cur.execute("SELECT PASSWORD FROM LOGIN where USERNAME=:u and FLAG=:u2",{"u":name,"u2":u1} )
        x=pass1.fetchone()[0]
        # con.close()
        # x1=x.index(0)
        print(x[0])
        if x==slot:
            return render_template("new_Admin.html")
        else:
            return "Failure Check Details"  
    except:
            
            msg = "Error In Sign In"
            return msg
      
    # finally:
    #         return "Finall"
    #         con.close()




@app.route('/SIGNUP', methods=['POST','GET'])
def signup():
    form2= request.form
    name1 =form2['uname1']
    slot1 = form2['psw1']
    u11=form2['typ1']


    print(name1 + slot1)

    try:
        con=sqlite3.connect('LOGIN.db')
        cur = con.cursor()
        count=cur.execute("INSERT INTO LOGIN (USERNAME,PASSWORD,FLAG) VALUES (?,?,?)",(name1,slot1,u11))
        con.commit()
        return "Success"
        con.close()  

    except:
        return "DB issue"  
        con.close()  



@app.route('/Results.html', methods=['POST','GET'])
def display():
    form1= request.form
    name =form1['sname']
    grade = form1['gr']

    

    try: 
        con=sqlite3.connect('STUDENT.db')
        cur = con.cursor()
        cur.execute("INSERT INTO STUD (NAME,GRADE) VALUES (?,?)",(name,grade) )
        con.commit()
        msg = "Record successfully added"
    except:
            
            msg = "error in insert operation"
      
    finally:
            return render_template("home.html",msg1=msg)
            con.close()


@app.route('/Results', methods=['POST','GET'])
def display1():
    form1= request.form
    name =form1['sname']
    grade = form1['gr']

    

    try: 
        con=sqlite3.connect('STUDENT.db')
        cur = con.cursor()
        cur.execute("INSERT INTO STUD (NAME,GRADE) VALUES (?,?)",(name,grade) )
        con.commit()
        msg = "Record successfully added"
    except:
            
            msg = "error in insert operation"
      
    finally:
            return render_template("Results.html",msg1=msg)
            con.close()


@app.route('/Delete', methods=['POST','GET'])
def Delete():
    form1= request.form
    ID =form1['DEL_ID']
    try: 
        con=sqlite3.connect('STUDENT.db')
        cur = con.cursor()
        count=cur.execute("select count(*) from STUD WHERE ID = :id1",{"id1":ID} )
        x=count.fetchone()
        try:
             x=x.index(0)
             msg="Id Not Present in Database Please check Using List All at Bottom"
                
        except:  
                con=sqlite3.connect('STUDENT.db')
                cur = con.cursor()
                cur.execute("DELETE FROM STUD WHERE ID = :id1",{"id1":ID} )
                con.commit()
                msg = "Record successfully Deleted"
        

    except:
            
             msg = "Error in Delete operation"
      
    finally:
            return render_template("Results.html",msg1=msg)
            con.close()  



   

@app.route('/Update', methods=['POST','GET'])
def update():
    form1= request.form
    ID =form1['UID']
    ugr1 =form1['ugr']

    try: 
        con=sqlite3.connect('STUDENT.db')
        cur = con.cursor()
        count=cur.execute("select count(*) from STUD WHERE ID = :id1",{"id1":ID} )
        x=count.fetchone()
        try:
             x=x.index(0)
             msg="Id Not Present in Database Please check Using List All at Bottom"
                
        except:  
                con=sqlite3.connect('STUDENT.db')
                cur = con.cursor()
                cur.execute("UPDATE STUD SET grade =:gr1 WHERE ID = :id1",{"gr1":ugr1,"id1":ID} )
                con.commit()
                msg = "Record successfully Updated"
        

    except:
            
             msg = "Error in Update operation"
      
    finally:
            return render_template("Results.html",msg1=msg)
            con.close()            
            
@app.route('/All', methods=['POST','GET'])
def All():

    try: 
        con=sqlite3.connect('STUDENT.db')
        cur = con.cursor()
        data=cur.execute("Select * from STUD" )
        con.commit()
        msg = "Record successfully Updated"
    except:
            
            msg = "Error in Update operation"
      
    finally:
            return render_template("Result.html",msg12=data)
            con.close()         
@app.route('/PASS', methods=['POST','GET'])
def PASS():

    try: 
        con=sqlite3.connect('STUDENT.db')
        cur = con.cursor()
        data=cur.execute("Select * from STUD where GRADE>=85" )
        con.commit()
        msg = "Record successfully Updated"
    except:
            
            msg = "Error in Update operation"
      
    finally:
            return render_template("Result.html",msg12=data)
            con.close()            

if __name__=="__main__":
    app.run(debug=True)    