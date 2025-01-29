from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Name: {name}, Email: {email}"
    else:
        return "Please submit the form."

if __name__ == '__main__':
    app.run(debug=False)
