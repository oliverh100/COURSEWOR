from app import db


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True)
#     email = db.Column(db.String(120), unique=True)
#     password_hash = db.Column(db.String(128))
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(64))
    s_name = db.Column(db.String(64))
    initials = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    title = db.Column(db.String(64))

    activities = db.relationship('Activity', secondary='teacher_activity_link')

    def iterable(self):
        return [self.f_name, self.s_name, self.initials, self.email, self.title]

    def add(self):
        db.session.add(self)
        db.session.commit()

    def edit(self, form):
        print(form.title.data, self.title)
        self.f_name = form.f_name.data
        self.s_name = form.s_name.data
        self.initials = form.initials.data
        self.email = form.email.data
        self.title = form.title.data
        print(form.title.data, self.title)
        db.session.commit()


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    r_name = db.Column(db.String(64))
    building = db.Column(db.String(64))

    activities = db.relationship('Activity', backref='room')


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a_name = db.Column(db.String(64))
    r_id = db.Column(db.Integer(), db.ForeignKey('room.id'))
    date_time = db.Column(db.String(64))
    max_attendees = db.Column(db.String(64))
    food_supplied = db.Column(db.String(64))

    teachers = db.relationship('Teacher', secondary='teacher_activity_link')


class TeacherActivityLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    t_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))


