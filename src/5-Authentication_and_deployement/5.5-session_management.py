from flask import Flask, redirect, url_for, render_template, request
from flask_login import LoginManager, login_user, logout_user, login_required

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used to encrypt session data

# In-memory storage for users
users = {'john_doe': 'password123'}  # A simple dictionary for user credentials

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return user_id
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if user exists and the password matches
        if username in users and users[username] == password:
            login_user(username)  # Log the user in
            return redirect(url_for('dashboard'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()  # Log the user out
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return 'Welcome to your dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
