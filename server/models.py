from sqlalchemy import sql, orm
from app import db

#TODO: Make everything lowercase rip
class Class(db.Model):
    __tablename__ = 'class'
    name = db.Column('name', db.String(100))
    class_id = db.Column('class_id', db.Integer, primary_key=True)
    department_id = db.Column('department_id', db.String(100), db.ForeignKey('department.department_id'), primary_key=True)
    class_num = db.Column('class_num', db.String(10))
    #booleans of whether or not the t-req is satisfied by this
    cz = db.Column('cz', db.Integer)
    ss = db.Column('ss', db.Integer)
    cci = db.Column('cci', db.Integer)
    alp = db.Column('alp', db.Integer)
    ns = db.Column('ns', db.Integer)
    qs = db.Column('qs', db.Integer)
    ei = db.Column('ei', db.Integer)
    fl = db.Column('fl', db.Integer)
    r = db.Column('r', db.Integer)
    sts = db.Column('sts', db.Integer)
    w = db.Column('w', db.Integer)

class Student(db.Model):
    __tablename__ = 'student'
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100), nullable=True)
    student_id = db.Column('student_id', db.Integer, primary_key=True)
    major = db.Column('major', db.String(100), db.ForeignKey('department.department_id'))

class Comment(db.Model):
    __tablename__ = "comment"
    text = db.Column('text', db.String(10000))
    upvotes = db.Column('upvotes', db.Integer)
    downvotes = db.Column('downvotes', db.Integer)
    student_id = db.Column('student_id', db.Integer, db.ForeignKey('student.student_id'))
    comment_id = db.Column('comment_id', db.Integer, primary_key=True)

class Department(db.Model):
    __tablename__ = 'department'
    #TODO: Update department_id to be a string
    name = db.Column('name', db.String(100))
    department_id = db.Column('department_id', db.String(100), primary_key=True)

class Taken(db.Model):
    __tablename__ = "taken"
    semester = db.Column('semester', db.String(4))
    star_number = db.Column("star_number", db.Float)
    comment_id = db.Column("comment_id", db.Integer, nullable=True)
    student_id = db.Column('student_id', db.Integer, db.ForeignKey('student.student_id'), primary_key=True)
    class_id = db.Column('class_id', db.Integer, db.ForeignKey('class.class_id'), primary_key=True)
    #TODO: This might be broken, idk if you can have a foreign key that is also nullable
    difficulty = db.Column("difficulty", db.Float)

class Professor(db.Model):
    __tablename__ = "professor"
    name = db.Column('name', db.String(100))
    professor_id = db.Column('professor_id', db.Integer, primary_key=True)

class Teaches(db.Model):
    __tablename__ = "teaches"
    class_id = db.Column('class_id', db.Integer, db.ForeignKey('class.class_id'), primary_key=True)
    professor_id = db.Column('professor_id', db.Integer, db.ForeignKey('professor.professor_id'),primary_key=True)
    semester = db.Column('semester', db.String(100), primary_key=True)
    average_quality = db.Column("average_quality", db.Float)
    average_difficulty = db.Column("average_difficulty", db.Float)
    num_reviews = db.Column("num_reviews", db.Integer)
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
