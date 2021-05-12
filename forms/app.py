from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField,DecimalField,SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date_ = DateField('Date', format='%Y')
    salary_= DecimalField('salary', places=2)
    fave_food= SelectField('your fav food', choices=[('indian','indian'),('chinese','chinese')])
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        date_= form.date_.data
        salary_=form.salary_.data
        fave_food=form.fave_food.data

        if len(first_name) == 0 or len(last_name) == 0 or not date_:
            error = "Please supply both first and last name and date"
        else:
            return f'thank_you {first_name}, you like {fave_food} food'

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')