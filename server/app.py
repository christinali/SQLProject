from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from full_classes import getFullClasses, getAllReviews
from condensed_classes import getMajors, getTreqs
from prof_info import getAllProfs
from flask_cors import CORS
import models
import forms
import sys

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})
CORS(app)

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
    if (user_id):
        return jsonify(getMajors())
    
@app.route('/get-recommended-treqs', methods=['GET'])
def gettreqs():
    user_id = request.args.get('user_id')
    if (user_id):
        return jsonify(getTreqs())
        
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
