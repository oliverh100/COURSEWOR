from flask import Flask, render_template, request, redirect, flash, url_for
from config import Config
from forms import LoginForm, MenuSelectionForm, AddTeacherForm, FindEditIdForm, EditTeacherForm, TeacherForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from fuzzywuzzy import fuzz

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
config = {
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}
app.config.from_mapping(config)
cache = Cache(app)

from models import Teacher, Activity, Room, TeacherActivityLink
from database_handling import TeacherOperations, edit_teacher


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = MenuSelectionForm()
    if form.validate_on_submit():
        return redirect(f'/{form.option.data}')
    return render_template('index.html', form=form)


# def do_add(form):
#     if form.validate_on_submit():
#         flash("Success add")
#         return redirect(url_for('.teachers'))
#
#
# def do_edit(form):
#     if form.validate_on_submit():
#         flash("Success edit")
#         return redirect(url_for('.teachers'))
#
#
# def do_edit_id(form):
#     if form.validate_on_submit():
#         flash("Success edit id")
#         teacher_id = find_id(form.s_name.data)
#         teacher_to_edit = Teacher.query.get(teacher_id)
#         edit_teacher_form.process(obj=teacher_to_edit)
#         cache.set('teacher_to_edit', teacher_to_edit)
#         return redirect(url_for('.teachers'))


@app.route('/teachers', methods=['GET', 'POST'])
def teachers():
    # result = None
    # add_teacher_form = None
    # edit_teacher_form = None
    # find_edit_id_form = None
    #
    # print(request.form)
    #
    # if 'submit_add' in request.form:
    #     add_teacher_form = AddTeacherForm()
    #     result = do_add(add_teacher_form)
    #
    # elif 'submit_edit' in request.form:
    #     edit_teacher_form = EditTeacherForm()
    #     result = do_edit(edit_teacher_form)
    #
    # elif 'submit_edit_id' in request.form:
    #     find_edit_id_form = FindEditIdForm()
    #     result = do_edit_id(find_edit_id_form)
    #
    # if result is not None:
    #     return result
    #
    # if add_teacher_form is None:
    #     add_teacher_form = AddTeacherForm(formdata=None)
    # if edit_teacher_form is None:
    #     edit_teacher_form = EditTeacherForm(formdata=None)
    # if find_edit_id_form is None:
    #     find_edit_id_form = FindEditIdForm(formdata=None)

    teacher_table = [teacher.iterable() for teacher in Teacher.query.all()]

    find_edit_id_form = FindEditIdForm()
    edit_teacher_form = EditTeacherForm()
    add_teacher_form = AddTeacherForm()
    teacher_form = TeacherForm()
    fields = ['f_name', 's_name', 'initials', 'email', 'title']

    if add_teacher_form.submit_add.data and add_teacher_form.validate_on_submit():
        print('g')
        new_teacher = TeacherOperations(
            Teacher(f_name=add_teacher_form.f_name.data, s_name=add_teacher_form.s_name.data, initials=add_teacher_form.initials.data,
                    email=add_teacher_form.email.data, title=add_teacher_form.title.data))
        new_teacher.add()

    if find_edit_id_form.submit_edit_id.data and find_edit_id_form.validate_on_submit():
        teacher_id = find_id(find_edit_id_form.s_name.data)
        teacher_to_edit = Teacher.query.get(teacher_id)
        edit_teacher_form.process(obj=teacher_to_edit)
        cache.set('teacher_to_edit', teacher_to_edit)
        return render_template('teachers.html', teacher_table=teacher_table, edit_teacher_form=edit_teacher_form, teacher_to_edit=teacher_to_edit,
                               find_edit_id_form=find_edit_id_form)

    if edit_teacher_form.submit_edit.data and edit_teacher_form.validate_on_submit():
        print('h')
        teacher_to_edit = cache.get('teacher_to_edit')
        # TeacherOperations(teacher_to_edit).edit(edit_teacher_form)
        # edit_teacher(teacher_to_edit, edit_teacher_form)
        print(edit_teacher_form.f_name.data, db)
        teacher_to_edit.f_name = edit_teacher_form.f_name.data
        db.session.commit()
        return redirect('teachers')

    teacher_table = [teacher.iterable() for teacher in Teacher.query.all()]
    return render_template('teachers.html', teacher_table=teacher_table, add_teacher_form=add_teacher_form, find_edit_id_form=find_edit_id_form,
                           edit_teacher_form=edit_teacher_form)


def find_id(name):
    best_ratio, t_id = 0, None
    for teacher in Teacher.query.all():
        if fuzz.ratio(name, teacher.s_name) > best_ratio:
            best_ratio, t_id = fuzz.ratio(name, teacher.s_name), teacher.id
    return t_id


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data))
#         return redirect('/index')
#     return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run()
