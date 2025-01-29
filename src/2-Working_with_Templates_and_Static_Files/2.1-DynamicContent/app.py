from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='Rahul')

@app.route('/items')
def items():
    return render_template('items.html', items=['Apple', 'Banana', 'Cherry'])


if __name__ == '__main__':
    app.run(debug=False)