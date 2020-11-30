from app import db
from models import Teacher, Activity, Room, TeacherActivityLink


class TeacherOperations(Teacher):
    def __init__(self, teacher):
        self.teacher = teacher

    def iterable(self):
        return [self.teacher.f_name, self.teacher.s_name, self.teacher.initials, self.teacher.email, self.teacher.title]

    def add(self):
        db.session.add(self.teacher)
        db.session.commit()

    def edit(self, form):
        print(form.title.data, self.teacher.title)
        self.teacher.f_name = form.f_name.data
        self.teacher.s_name = form.s_name.data
        self.teacher.initials = form.initials.data
        self.teacher.email = form.email.data
        self.teacher.title = form.title.data
        print(form.title.data, self.teacher.title)
        db.session.commit()


def edit_teacher(teacher, form):
    print(db)
    print(teacher.id, form.f_name.data)
    teacher.f_name = form.f_name.data
    teacher.s_name = form.s_name.data
    teacher.initials = form.initials.data
    teacher.email = form.email.data
    teacher.title = form.title.data
    db.session.commit()
