from sqlalchemy import sql, orm
from app import db

#TODO: Make everything lowercase rip
class Class(db.Model):
    __tablename__ = 'class'
    name = db.Column('name', db.String(100))
    class_id = db.Column('class_id', db.Integer, primary_key=True)
    department_id = db.Column('department_id', db.Integer, db.ForeignKey('department.department_id'), primary_key=True)
    #booleans of whether or not the t-req is satisfied by this
    # cz = db.Column('cz', db.Integer)
    # ss = db.Column('ss', db.Integer)
    # cci = db.Column('cci', db.Integer)

class Student(db.Model):
    __tablename__ = 'student'
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100), nullable=True)
    student_id = db.Column('student_id', db.Integer, primary_key=True)
    major = db.Column('major', db.String(100), db.ForeignKey('department.name'))

class Comment(db.Model):
    __tablename__ = "comment"
    text = db.Column('text', db.String(10000))
    upvotes = db.Column('upvotes', db.Integer)
    downvotes = db.Column('downvotes', db.Integer)
    student_id = db.Column('student_id', db.Integer, db.ForeignKey('student.studentID'))
    comment_id = db.Column('comment_id', db.Integer, primary_key=True)

class Department(db.Model):
    __tablename__ = 'department'
    name = db.Column('name', db.String(100))
    department_id = db.Column('department_id', db.Integer, primary_key=True)

class Taken(db.Model):
    __tablename__ = "taken"
    semester = db.Column('semester', db.String(4))
    star_number = db.Column("star_number", db.Float)
    comment_id = db.Column("comment_id", db.Integer, nullable=True)
    student_id = db.Column('student_id', db.Integer, db.ForeignKey('student.studentID'), primary_key=True)
    class_id = db.Column('class_id', db.Integer, db.ForeignKey('class.classID'), primary_key=True)
    #TODO: This might be broken, idk if you can have a foreign key that is also nullable
    department_id = db.Column('department_id', db.Integer, db.ForeignKey('department.department_id'), primary_key=True)

class Professor(db.Model):
    __tablename__ = "professor"
    name = db.Column('name', db.String(100))
    professor_id = db.Column('professor_id', db.Integer, primary_key=True)

class Teaches(db.Model):
    __tablename__ = "teaches"
    class_id = db.Column('class_id', db.Integer, db.ForeignKey('class.classID'), primary_key=True)
    professor_id = db.Column('professor_id', db.Integer, db.ForeignKey('professor.professorID'),primary_key=True)
    semester = db.Column('semester', db.String(4))

# class Drinker(db.Model):
#     __tablename__ = 'drinker'
#     name = db.Column('name', db.String(20), primary_key=True)

#     likes = orm.relationship('Likes')
#     frequents = orm.relationship('Frequents')
#     @staticmethod
#     def edit(old_name, name, address, beers_liked, bars_frequented):
#         try:
#             db.session.execute('DELETE FROM likes WHERE drinker = :name',
#                                dict(name=old_name))
#             db.session.execute('DELETE FROM frequents WHERE drinker = :name',
#                                dict(name=old_name))
#             db.session.execute('UPDATE drinker SET name = :name, address = :address'
#                                ' WHERE name = :old_name',
#                                dict(old_name=old_name, name=name, address=address))
#             for beer in beers_liked:
#                 db.session.execute('INSERT INTO likes VALUES(:drinker, :beer)',
#                                    dict(drinker=name, beer=beer))
#             for bar, times_a_week in bars_frequented:
#                 db.session.execute('INSERT INTO frequents'
#                                    ' VALUES(:drinker, :bar, :times_a_week)',
#                                    dict(drinker=name, bar=bar,
#                                         times_a_week=times_a_week))
#             db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise e

# class Beer(db.Model):
#     __tablename__ = 'beer'
#     name = db.Column('name', db.String(20), primary_key=True)
#     brewer = db.Column('brewer', db.String(20))

# class Bar(db.Model):
#     __tablename__ = 'bar'
#     name = db.Column('name', db.String(20), primary_key=True)
#     address = db.Column('address', db.String(20))
#     serves = orm.relationship('Serves')

# class Likes(db.Model):
#     __tablename__ = 'likes'
#     drinker = db.Column('drinker', db.String(20),
#                         db.ForeignKey('drinker.name'),
#                         primary_key=True)
#     beer = db.Column('beer', db.String(20),
#                      db.ForeignKey('beer.name'),
#                      primary_key=True)

# class Serves(db.Model):
#     __tablename__ = 'serves'
#     bar = db.Column('bar', db.String(20),
#                     db.ForeignKey('bar.name'),
#                     primary_key=True)
#     beer = db.Column('beer', db.String(20),
#                      db.ForeignKey('beer.name'),
#                      primary_key=True)
#     price = db.Column('price', db.Float())

# class Frequents(db.Model):
#     __tablename__ = 'frequents'
#     drinker = db.Column('drinker', db.String(20),
#                         db.ForeignKey('drinker.name'),
#                         primary_key=True)
#     bar = db.Column('bar', db.String(20),
#                     db.ForeignKey('bar.name'),
#                     primary_key=True)
#     times_a_week = db.Column('times_a_week', db.Integer())