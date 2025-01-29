from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///activity_6.db'
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

@app.route('/query-all')
def query_all():
    users = User.query.all()
    return "<br>".join([f"{user.username}: {user.email}" for user in users])

@app.route('/query-filter/<username>')
def query_filter(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return f"Found User: {user.username} - {user.email}"
    return "User not found!"

@app.route('/query-order')
def query_order():
    users = User.query.order_by(User.username).all()
    return "<br>".join([f"{user.username}: {user.email}" for user in users])

if __name__ == '__main__':
    app.run(debug=True)
