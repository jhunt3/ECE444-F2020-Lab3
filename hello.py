from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = '8ij09trdjki'
bootstrap = Bootstrap(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    email = StringField('What is your U of T email address?', validators=[Email()])
    submit = SubmitField('Submit')
@app.route('/', methods=['GET', 'POST'])
def index():

    name = None
    form = NameForm()

    if form.validate_on_submit():
        old_name = session.get('name')
        email_address = form.email.data
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if 'utoronto' not in email_address:
            flash('That is not a U of T account!')
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))
    return render_template('index.html',
        form=form, name=session.get('name'), email=session.get('email'))
@app.route('/user/<name>')
def user(name):
    currentTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return render_template('user.html',name=name, currentDateTime=currentTime)
#app.run(host='0.0.0.0', port=5000)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)