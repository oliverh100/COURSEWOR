from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class MenuSelectionForm(FlaskForm):
    option = RadioField(u'Choice', choices=[('teachers', 'teachers'), ('rooms', 'rooms'), ('activities', 'activities')], validate_choice=False)


class AddTeacherForm(FlaskForm):
    f_name = StringField('First name', validators=[DataRequired()])
    s_name = StringField('Surname', validators=[DataRequired()])
    initials = StringField('Initials', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    submit_add = SubmitField('Submit')


class FindEditIdForm(FlaskForm):
    s_name = StringField('Surname', validators=[DataRequired()])
    submit_edit_id = SubmitField('Submit')


class EditTeacherForm(FlaskForm):
    f_name = StringField('First name', validators=[DataRequired()])
    s_name = StringField('Surname', validators=[DataRequired()])
    initials = StringField('Initials', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    submit_edit = SubmitField('Submit')


class TeacherForm(FlaskForm):
    f_name = StringField('First name', validators=[DataRequired()])
    s_name = StringField('Surname', validators=[DataRequired()])
    initials = StringField('Initials', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')
