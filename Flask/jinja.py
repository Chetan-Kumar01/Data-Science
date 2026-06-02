from flask import Flask, render_template, request, redirect, url_for
from flask import url_for
'''
It creates an instance of the Flask class,
which will be your WSGI application.
'''
## WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "<html><h1>Welcome to the flask course. This is the welcome page.</h1></html>"

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about(): 
    return render_template('about.html')



## Variable Rule
## @app.route('/success/<int:score>')
## def success(score):
##    return f'Your score is {str(score)}!'

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score,'res':res}

    return render_template('result1.html',results=exp)

@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result.html',results=score)

## Dynamic url
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form.get('science'))
        maths=float(request.form.get('maths'))
        c=float(request.form.get('c'))
        datascience=float(request.form.get('datascience'))

        total_score=(science+maths+c+datascience)/4
    
        return redirect(url_for('successres',score=total_score))
    return render_template('getresult.html')



if __name__ == '__main__':
    app.run(debug=True)