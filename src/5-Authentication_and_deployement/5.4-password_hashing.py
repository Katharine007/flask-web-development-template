from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/hash-password/<password>')
def hash_password(password):
    hashed_password = generate_password_hash(password)
    return f"Hashed password: {hashed_password}"

@app.route('/check-password/<hashed_password>/<password>')
def check_password(hashed_password, password):
    if check_password_hash(hashed_password, password):
        return "Password matches"
    return "Password does not match"

if __name__ == '__main__':
    app.run(debug=True)
