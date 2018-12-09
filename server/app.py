from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from full_classes import getFullClasses, getAllReviews
from condensed_classes import getMajors, getTreqs
from prof_info import getAllProfs
from flask_cors import CORS
import models
import forms
import sys
import math

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})
CORS(app)

@app.route('/', methods=['GET'])
def dontReach():
    return '"DONT REACH" - Feroze'

@app.route('/departments', methods=['GET'])
def getAllDepartments():
    departments = db.session.query(models.Department).all()
    departmentList = dict()
    for department in departments:
        departmentList[department.department_id] = department.name
    return jsonify(departmentList)

@app.route('/get-id', methods=['GET'])
def getId():
    email = request.args.get('email')
    if (email):
        return "0"

@app.route('/create-user', methods=['GET', 'POST'])
def createUser():
    first = request.args.get('first')
    last = request.args.get('last')
    email = request.args.get('email')
    year = request.args.get('year')
    major = request.args.get('major')
    if (first and last and email and year and major):
        return "0"

@app.route('/add-class', methods=['GET', 'POST'])
def addClass():
    user_id = request.args.get('user_id')
    class_id = request.args.get('class_id')
    sem = request.args.get('sem')
    year = request.args.get('year')
    if (user_id and class_id and sem and year):
        return "Added"

@app.route('/get-curr-classes', methods=['GET'])
def getClasses():
    user_id = request.args.get('user_id')
    if (user_id):
        return jsonify(getFullClasses())

@app.route('/get-recommended-major', methods=['GET'])
def getRecommendedMajorClasses():
    user_id = request.args.get('user_id')
    major = findUserMajor(user_id)
    department_id = db.session.query(models.Department).filter_by(department_id=major).first().department_id
    classesInMajor = db.session.query(models.Class).filter_by(department_id=department_id).all()
    classList = list()
    for i,eachClass in enumerate(classesInMajor):
        classList.append(dict())
        classList[i]['dept'] = major
        classList[i]['overall'] = getRating(eachClass.class_id)
        classList[i]['difficulty'] = getDifficulty(eachClass.class_id)
        classList[i]['name'] = eachClass.name
        classList[i]['id'] = eachClass.class_id
        classList[i]['num'] = eachClass.class_num
    classList = sorted(classList, key=cmp_to_key(compareClasses))
    return jsonify(classList)


@app.route('/get-all-majors', methods=['GET'])
def getAllMajors():
    majors = list()
    alldeps = db.session.query(models.Department).all()
    for dep in alldeps:
        majors.append(dep.department_id)
    return jsonify(majors)

def getRating(class_id):
    takenTuples = db.session.query(models.Taken).filter_by(class_id=class_id).all()
    notNull = db.session.query(models.Taken, models.Comment).filter_by(class_id=class_id).join().all()
    totalUpvotes = 0
    totalDownvotes = 0
    for comment in notNull:
        totalUpvotes +=comment.Comment.upvotes
        totalDownvotes += comment.Comment.downvotes
    ratings = list()
    for taken in takenTuples:
        if taken.comment_id is not None:
            #should probably optimize
            comment = db.session.query(models.Comment).filter_by(comment_id=taken.comment_id).first()
            numUpvotes = comment.upvotes
            numDownvotes = comment.downvotes
            timesToAppend = int(math.log(1/(1-numUpvotes/totalUpvotes+.00000001),2))
            timesToAppend -= int(math.log(1/(1-numDownvotes/totalDownvotes+.00000001),2))
            for i in range(timesToAppend):
                ratings.append(taken.star_number)
        ratings.append(taken.star_number)
    total = 0
    for rating in ratings:
        total+=rating
    if len(ratings)==0:
        return 2.5
    return total/len(ratings)

def getDifficulty(class_id):
    takenTuples = db.session.query(models.Taken).filter_by(class_id=class_id).all()
    notNull = db.session.query(models.Taken, models.Comment).filter_by(class_id=class_id).join().all()
    totalUpvotes = 0
    totalDownvotes = 0
    for comment in notNull:
        totalUpvotes +=comment.Comment.upvotes
        totalDownvotes += comment.Comment.downvotes
    difficulties = list()
    for taken in takenTuples:
        if taken.comment_id is not None:
            #should probably optimize
            comment = db.session.query(models.Comment).filter_by(comment_id=taken.comment_id).first()
            numUpvotes = comment.upvotes
            numDownvotes = comment.downvotes
            timesToAppend = int(math.log(1/(1-numUpvotes/totalUpvotes+.00000001),2))
            timesToAppend -= int(math.log(1/(1-numDownvotes/totalDownvotes+.00000001),2))
            for i in range(timesToAppend):
                difficulties.append(taken.difficulty)
        difficulties.append(taken.difficulty)
    total = 0
    for rating in difficulties:
        total+=rating
    if len(difficulties)==0:
        return 2.5
    return total/len(difficulties)

def findUserMajor(user_id):
    student = db.session.query(models.Student).filter_by(student_id=user_id).first()
    return student.major

requirements = {'cz':2, 'alp':2,'ns':2}
requirements = ['cz', 'alp', 'ns']

def getCompleted(user_id):
    classesTaken = db.session.query(models.Taken).filter_by(student_id=user_id).all()
    completed = dict()
    for eachClass in classesTaken:
        classItself = db.session.query(models.Class).filter_by(class_id=eachClass.class_id).first()
        if classItself.alp == 1:
            if 'alp' not in completed:
                completed['alp']=0
            completed['alp']+=1
        if classItself.ns == 1:
            if 'ns' not in completed:
                completed['ns']=0
            completed['ns']+=1
        if classItself.cz == 1:
            if 'cz' not in completed:
                completed['cz']=0
            completed['cz']+=1
    return completed

def getClassesWithReqs(needed):
    classes = dict()
    if 'alp' in needed:
        currClasses = db.session.query(models.Class).filter_by(alp=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('alp')
    if 'ns' in needed:
        currClasses = db.session.query(models.Class).filter_by(ns=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('ns')
    if 'cz' in needed:
        currClasses = db.session.query(models.Class).filter_by(cz=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('cz')
    return classes

#TODO: run a difference query so that you don't recommend classes people have taken already
@app.route('/get-recommended-treqs', methods=['GET'])
def gettreqs():
    user_id = request.args.get('user_id')
    completed = getCompleted(user_id)
    needed = ['alp','alp', 'cz', 'cz','ns', 'ns']
    for key in completed:
        if completed[key]>=2:
            needed.remove(key)
            needed.remove(key)
    classList = list()
    classesWithReqs = getClassesWithReqs(needed)
    for i,eachClass in enumerate(classesWithReqs.keys()):
        classList.append(dict())
        classList[i]['dept'] = eachClass.department_id
        classList[i]['overall'] = getRating(eachClass.class_id)
        classList[i]['difficulty'] = getDifficulty(eachClass.class_id)
        classList[i]['name'] = eachClass.name
        classList[i]['id'] = eachClass.class_id
        classList[i]['num'] = eachClass.class_num
        classList[i]['satisfiesNeeded'] = classesWithReqs[eachClass]
        # temp = list()
        # for req in classList[i]['satisfiesNeeded']:
        #     if req not in completed or completed[req]==0:
        #         temp.append(req)
        #         app.logger.warning(req)
        # for t in temp:
        #     classList[i]['satisfiesNeeded'].append(t)
    classList = sorted(classList, key=cmp_to_key(compareClasses))
    return jsonify(classList)

def score(currClass):
    score = 0
    score += currClass['overall']
    score-=currClass['difficulty']
    if 'satisfiesNeeded' in currClass:
        score+=len(currClass['satisfiesNeeded'])
    return score

def compareClasses(class1, class2):
    return score(class2) - score(class1)

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

@app.route('/get-class-info', methods=['GET'])
def getClassInfo():
    class_id = request.args.get('class_id')
    return jsonify(getFullClasses()[int(class_id)])

@app.route('/get-prof-info', methods=['GET'])
def getProfInfo():
    prof_id = request.args.get('prof_id')
    return jsonify(getAllProfs()[int(prof_id)])

@app.route('/get-all-classes', methods=['GET'])
def getAllClasses():
    return jsonify(getFullClasses())

@app.route('/get-all-reviews', methods=['GET'])
def getReviews():
    class_id = request.args.get('class_id')
    if (class_id):
        return jsonify(getAllReviews())

@app.route('/reviews/upvote', methods=['GET', 'POST'])
def upvote():
    review_id = request.args.get('review_id')
    if (review_id):
        curr = getAllReviews()[int(review_id)].get("up")
        return jsonify(int(curr) + 1)

@app.route('/reviews/downvote', methods=['GET', 'POST'])
def downvote():
    review_id = request.args.get('review_id')
    if (review_id):
        curr = getAllReviews()[int(review_id)].get("down")
        return jsonify(int(curr) + 1)

@app.route('/get-full-class', methods=['GET'])
def getFullClass():
    class_id = request.args.get('class_id')
    fullClass = dict()
    for c in getFullClasses():
        if (c.get("id") == class_id):
            fullClass = c
    return jsonify(fullClass)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
