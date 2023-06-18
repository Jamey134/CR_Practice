from flask import Flask, render_template, request, redirect, session
from user_model import Users
# from flask_session import Session

app = Flask(__name__)
app.secret_key = "TOPSECRET"


@app.route('/')
def newUsers():
    return redirect ('/users/new')


@app.route('/users')
def users():
    return render_template('users.html', users=Users.get_all())

@app.route('/users/new')
def new():
    return render_template('new_users.html')


@app.route('/users/added', methods=['POST'])
def add():
    print("Got Post Info")
    Users.save(request.form)
    
    # data = {
    #     "first_name": request.form['first_name'],
    #     "last_name": request.form['last_name'],
    #     'email': request.form['email']
    # }
    # Users.save(data)


    return redirect('/users')



if __name__ == "__main__":
    app.run(debug=True, port=5005)
