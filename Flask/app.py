from flask import Flask
'''
It creates an instance of the Flask class,
which will be your WSGI application.
'''
## WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask App! This Should be an Amazing course."

@app.route('/index')
def index():
    return "This is the index page of the Flask App."

if __name__ == '__main__':
    app.run(debug=True)
