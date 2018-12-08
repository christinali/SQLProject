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
def getmajors():
    user_id = request.args.get('user_id')
    major = findUserMajor(user_id)
    department_id = db.session.query(models.Department).filter_by(name=major).first().department_id
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
    return jsonify(classList)

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
    return total/len(difficulties)

def findUserMajor(user_id):
    student = db.session.query(models.Student).filter_by(student_id=user_id).first()
    return student.major

@app.route('/get-recommended-treqs', methods=['GET'])
def gettreqs():
    user_id = request.args.get('user_id')
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
    return jsonify(classList)

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
