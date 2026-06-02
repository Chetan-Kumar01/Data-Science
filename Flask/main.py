from flask import Flask, render_template, request
'''
It creates an instance of the Flask class,
which will be your WSGI application.
'''

## Jinja2 template engine
'''
{{ }} expressions to print output in html
{%...%} conditions , for loops
{#...#} comments
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

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form.get('name')
        gender=request.form.get('gender')
 
        if not name or not gender:
            error="⚠️ Please fill all fields before submitting it"
            return render_template('form.html',error=error)
        return render_template('success.html',name=name, gender=gender)
    return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True)
