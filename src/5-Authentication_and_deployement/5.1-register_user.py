from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Dummy user storage (in-memory)
users = {}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        users[username] = hashed_password  # Save username and hashed password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login')
def login():
    return 'Redirected to login page'

if __name__ == '__main__':
    app.run(debug=True)
