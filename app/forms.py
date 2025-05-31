from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', 
                         validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', 
                                   validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Роль', 
                      choices=[
                          ('admin', 'Администратор'),
                          ('librarian', 'Библиотекарь'),
                          ('reader', 'Читатель'),
                          ('analyst', 'Аналитик'),
                          ('guest', 'Гость')
                      ], 
                      validators=[DataRequired()])
    submit = SubmitField('Зарегистрировать')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Это имя пользователя уже занято.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Этот email уже используется.')

class BookForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    author = StringField('Автор', validators=[DataRequired()])
    year = IntegerField('Год издания', validators=[DataRequired()])
    genre = StringField('Жанр', validators=[DataRequired()])
    submit = SubmitField('Сохранить')

class SearchForm(FlaskForm):
    search_query = StringField('Поиск', validators=[DataRequired()])
    submit = SubmitField('Найти')