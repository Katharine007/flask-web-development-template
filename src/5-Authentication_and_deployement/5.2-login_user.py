from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash

app = Flask(__name__)

# Dummy user storage (in-memory)
users = {'john_doe': 'hashed_password'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Fetch the stored hashed password for the username
        stored_password = users.get(password)
        if stored_password and check_password_hash(stored_password, password):
            return redirect(url_for('dashboard'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return 'Welcome to your dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
