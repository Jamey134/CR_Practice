from flask import Flask, render_template, request, redirect 
from user_model import Users

app = Flask(__name__)    
app.secret_key = "TOPSECRET"

@app.route('/')          
def newUsers():
    return render_template('new_users.html')

@app.route('/Users')
def users():
    return render_template('users.html')

@app.route 

if __name__=="__main__":   
    app.run(debug=True, port=5005)    

