from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('lab7.html')

@app.route('/lab7.html')
def dis():
    return render_template('lab7.html')


@app.route('/Results.html', methods=['POST','GET'])
def display():
    form1= request.form
    username=form1['sname']
    passw=form1['pwd']

    if request.method=='POST':
        return render_template('Results.html',dat=passw)

 
# main driver function
if __name__ == '__main__':
   app.run(debug = True)