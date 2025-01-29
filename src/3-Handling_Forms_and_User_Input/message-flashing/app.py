from flask import Flask, flash, redirect, url_for, render_template

app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Add a unique and secure secret key here.

@app.route('/submit', methods=['POST'])
def submit_form():
    # Process the form data
    flash('Form submitted successfully!')
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting the form!"

if __name__ == '__main__':
    app.run(debug=False)