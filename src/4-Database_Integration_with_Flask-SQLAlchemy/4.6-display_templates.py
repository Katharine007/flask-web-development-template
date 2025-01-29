from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///activity_7.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/create-users')
def create_users():
    with app.app_context():
        db.create_all()
        users = [
            User(username='john_doe', email='john@example.com'),
            User(username='jane_doe', email='jane@example.com'),
            User(username='alice', email='alice@example.com'),
        ]
        db.session.bulk_save_objects(users)
        db.session.commit()
    return "Users created successfully!"

@app.route('/display-users')
def display_users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
