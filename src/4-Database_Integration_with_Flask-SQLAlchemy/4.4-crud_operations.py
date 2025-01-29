from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///activity_4.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Route to initialize the database and create tables
@app.route('/init-db')
def init_db():
    with app.app_context():
        db.create_all()
    return "Database and tables created!"

@app.route('/add-user')
def add_user():
    new_user = User(username='john_doe', email='john@example.com')
    db.session.add(new_user)
    db.session.commit()
    return "User added to the database!"

@app.route('/read-user')
def read_user():
    user = User.query.filter_by(username='john_doe').first()
    if user:
        return f"Read User: {user.username}, {user.email}"
    return "User not found!"

@app.route('/update-user')
def update_user():
    user = User.query.filter_by(username='john_doe').first()
    if user:
        user.email = 'updated_email@example.com'
        db.session.commit()
        return "User updated successfully!"
    return "User not found!"

@app.route('/delete-user')
def delete_user():
    user = User.query.filter_by(username='john_doe').first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return "User deleted successfully!"
    return "User not found!"

if __name__ == '__main__':
    app.run(debug=True)
