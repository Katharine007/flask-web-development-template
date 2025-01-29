from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    return f"Name: {name}, Email: {email}"

if __name__ == '__main__':
    app.run(debug=False)
