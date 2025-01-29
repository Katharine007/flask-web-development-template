from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    form = MyForm()
    if form.validate_on_submit():
        return f"Name: {form.name.data}, Email: {form.email.data}"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
