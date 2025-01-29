from flask import Flask

app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=False)