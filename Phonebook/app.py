import os
from flask import Flask, Blueprint, render_template, redirect, request, session, url_for, jsonify

app = Flask(__name__)
app.config['secret_key'] = 'strangerthings'

imageFolder = os.path.join('static', 'image')

app.config['UPLOAD_FOLDER'] = imageFolder

@app.route("/")
def index():
    business = os.path.join(app.config['UPLOAD_FOLDER'], 'business.png')
    return render_template("index.html", user_image = business)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

def __repr__(self):
    return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Christopher', password='password'))
users.append(User(id=1, username='Lawson', password='secret'))

@app.before_request
def before_request():
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        
        return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)