from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
Bootstrap(app)

# Функция для валидации уникальных цифр
def unique_digits(form, field):
    digits = str(field.data)
    if len(set(digits)) != len(digits):
        raise ValidationError("Число не должно содержать повторяющихся цифр.")

class NumberForm(FlaskForm):
    number = IntegerField('Введите целое положительное число:', 
                          validators=[DataRequired(), NumberRange(min=1), unique_digits])
    submit = SubmitField('Проверить')

@app.route('/', methods=['GET', 'POST'])
def input_number():
    form = NumberForm()
    if form.validate_on_submit():
        flash("Число состоит из уникальных цифр!", "success")
        return redirect(url_for('result'))
    return render_template('input.html', form=form)

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
