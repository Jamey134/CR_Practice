from flask import Flask, render_template, request, redirect, session
from user_model import Users
from flask_session import Session

app = Flask(__name__)
app.secret_key = "TOPSECRET"


@app.route('/')
def newUsers():
    return redirect ('/users')


@app.route('/users')
def users():
    return render_template('users.html')

@app.routh('/users/new')
def new():
    return render_template()


@app.route('/users/added', methods=['POST'])
def add():
    print("Got Post Info")
    session['userID'] = request.form['id']
    session['userFirstName'] = request.form.get('first_name')
    session['userLastName'] = request.form['last_name']
    session['userEmail'] = request.form['email']
    
    return redirect('/users')



if __name__ == "__main__":
    app.run(debug=True, port=5005)
