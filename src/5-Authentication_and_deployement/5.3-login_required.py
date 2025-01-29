from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user storage (in-memory)
users = {'john_doe': 'hashed_password'}

login_manager = LoginManager()
login_manager.init_app(app)

# Dummy current user
current_user = None

@app.route('/login', methods=['GET', 'POST'])
def login():
    global current_user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Fetch the stored hashed password for the username
        stored_password = users.get(username)
        if stored_password and check_password_hash(stored_password, password):
            current_user = username  # Set the current user
            return redirect(url_for('dashboard'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return 'Welcome to your dashboard!'

@login_manager.user_loader
def load_user():
    return current_user

if __name__ == '__main__':
    app.run(debug=True)
