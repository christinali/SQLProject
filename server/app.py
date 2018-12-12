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
import csv
import sqlalchemy
from sqlalchemy.sql import exists
from sqlalchemy.sql.expression import cast

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})
CORS(app)
lastIds = [i for i in range(10)]


@app.route('/', methods=['GET'])
def dontReach():
    return '"DONT REACH" - Feroze'

@app.route('/get-user-classes', methods=['GET'])
def getUserClasses():
    user_id = request.args.get('user_id')
    allClasses = list()
    if (user_id):
        taken = db.session.query(models.Taken).filter_by(student_id=user_id).all()
        for eachTaken in taken:
            classes = db.session.query(models.Class).filter_by(class_id=eachTaken.class_id).all()
            for eachClass in classes:
                allClasses.append({"name": eachClass.name, "id": eachClass.class_id,
                 "dept": eachClass.department_id, "class_num": eachClass.class_num})
    return jsonify(allClasses)






@app.route('/longclasses', methods=['GET'])
def longclasses():
    with open('/Users/moboyle769/Documents/compsci316/project/sqlproject/classes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        res = []
        for line in csv_reader:
            res.append(line)
        return jsonify(res)

@app.route('/longprofs', methods=['GET'])
def longprofs():
    with open('/Users/moboyle769/Documents/compsci316/project/sqlproject/profs.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        res = []
        for line in csv_reader:
            res.append(line)
        return jsonify(res)

@app.route('/test', methods=['GET'])
def test():
    ins = db.insert(models.Professor).values(professor_id='123456789', name='Testing test test')
    print(ins)




@app.route('/longteaches', methods=['GET'])
def longteaches():
    with open('/Users/moboyle769/Documents/compsci316/project/sqlproject/teaches.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        res = []
        for line in csv_reader:
            res.append(line)
        return jsonify(res)

@app.route('/longdepts', methods=['GET'])
def longdepts():
    with open('/Users/moboyle769/Documents/compsci316/project/sqlproject/departments.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        res = []
        for line in csv_reader:
            res.append(line)
        return jsonify(res)

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
        return jsonify(emailToId(email))

def emailToId(email):
    ids = db.session.query(models.Student).filter_by(email=email).all()
    student_id = 0
    for id in ids:
        student_id = id.student_id
    return student_id


@app.route('/create-user', methods=['GET', 'POST'])
def createUser():
    name = request.args.get('name')
    email = request.args.get('email')
    year = request.args.get('year')
    major = request.args.get('major')
    year = year[-1]
    year = int(year)
    if (name and email and year and major):
        while db.session.query(models.Student).filter_by(student_id=lastIds[year]).first():
            lastIds[year]+=10
        newUser = models.Student(name=name, email=email, student_id=lastIds[year], major=major)
        db.session.add(newUser)
        db.session.commit()
        lastIds[year]+=10
        return "Successfully created new user"
    return "Need to give name, user, year, and major, but not all inputs were given"

@app.route('/feroze-create-user', methods=['GET', 'POST'])
def createFeroze():
    req_data = request.get_json()
    first = req_data['first']
    last = req_data['last']
    email = req_data['email']
    year = req_data['grad_year'] #2020
    major = req_data['major']
    if (first and last and email and year): ## this gets replaced by find user_id
        return "1"
    return "0"

# @app.route('/add-class', methods=['GET', 'POST'])
# def addClass():
#     user_id = request.args.get('user_id')
#     class_id = request.args.get('class_id')
#     semester = request.args.get('semester')
#     star_number = request.args.get('star_number')
#     comment_id = request.args.get('comment_id')
#     difficulty = request.args.get('difficulty')
#     print(user_id)
#     print(class_id)
#     print(department_id)
#     print(semester)
#     print(start_number)
#     print(difficulty)
#     print("\n\n\n\n\n\n")
    # if (user_id and class_id and department_id and semester and star_number and difficulty):
    #     print(user_id)
    #     print(class_id)
    #     print(department_id)
    #     print(semester)
    #     print(start_number)
    #     print(difficulty)
    #     print("\n\n\n\n\n\n")
    #
    #     if not comment_id:
    #         newTaken = models.Taken(semester=semester,star_number=star_number,student_id=user_id,class_id=class_id,department_id=department_id,difficulty=difficulty)
    #     else:
    #         newTaken = models.Taken(semester=semester,star_number=star_number,student_id=user_id,class_id=class_id,department_id=department_id,difficulty=difficulty,comment_id=comment_id)
    #     db.session.add(newTaken)
    #     db.session.commit()
    #     print("YEAH\n\n\n\n\n")
    #     return "Success!"
    # print("NOPE\n\n\n\n")
    # return "Failure"

def createComment():
    comments = list()
    classesInMajor = db.session.query(models.Comment).all()



@app.route('/add-class', methods=['GET', 'POST'])
def addClass():
    user_id = int(request.args.get('user_id'))
    dept_id = request.args.get('dept')
    num = request.args.get('class_num')
    class_id = 0
    semester = request.args.get('semester')
    star_number = float(request.args.get('star_number'))
    comment = request.args.get('comment')
    ids = db.session.query(models.Class).filter(models.Class.department_id==dept_id).filter(models.Class.class_num==num).all()
    for id in ids:
        class_id = id.class_id


    difficulty = float(request.args.get('difficulty'))
    if (user_id and class_id and semester and star_number and difficulty):
        if not comment:
            newTaken = models.Taken(semester=semester,star_number=star_number,student_id=user_id,class_id=class_id,difficulty=difficulty)
        else:
            commentId = createComment(comment)
            newTaken = models.Taken(semester=semester,star_number=star_number,student_id=user_id,class_id=class_id,department_id=department_id,difficulty=difficulty,comment_id=comment_id)
        db.session.add(newTaken)
        db.session.commit()
        return "Success!"
    return "Need to give name, user, year, and major, but not all inputs were given"

@app.route('/feroze-add-class', methods=['GET', 'POST'])
def addFakeClass():
    req_data = request.get_json()

    user_id = req_data['user_id']
    department_id = req_data['dept_id']
    class_num = req_data['class_num']
    semester = req_data['semester'] #'2013 Spring Term'
    star_number = req_data['star_number']
    comment_id = req_data['comment_id']
    difficulty = req_data['difficulty']
    if (user_id and department_id and class_num and semester and star_number and difficulty):
        return '200'
    return '404'

@app.route('/get-curr-classes', methods=['GET'])
def getClasses():
    user_id = request.args.get('user_id')
    if (user_id):
        return jsonify(getFullClasses())

@app.route('/get-recommended-major', methods=['GET'])
def getRecommendedMajorClasses():
    email = request.args.get('email')
    user_id = emailToId(email)
    major = findUserMajor(user_id)
    # department_id = db.session.query(models.Department).filter_by(department_id=major).first().department_id
    classesInMajor = db.session.query(models.Class).filter_by(department_id=major).all()
    classList = list()
    takenAlready = db.session.query(models.Taken).filter_by(student_id=user_id).all()
    haveTaken = set()
    for taken in takenAlready:
        haveTaken.add(taken.class_id)
    i = 0
    for _,eachClass in enumerate(classesInMajor):
        if eachClass.class_id in haveTaken:
            continue
        classList.append(dict())
        classList[i]['dept'] = major
        classList[i]['overall'] = round(getRating(eachClass.class_id),2)
        classList[i]['difficulty'] = round(getDifficulty(eachClass.class_id),2)
        classList[i]['name'] = eachClass.name
        classList[i]['id'] = eachClass.class_id
        classList[i]['num'] = eachClass.class_num
        classList[i]['satisfiesNeeded'] = returnAllTreqs(eachClass)
        i+=1
    classList = sorted(classList, key=cmp_to_key(compareClasses))
    return jsonify(classList)

def returnAllTreqs(eachClass):
    allTreqs = list()
    if eachClass.cz:
        allTreqs.append("cz")
    if eachClass.ss:
        allTreqs.append("ss")
    if eachClass.cci:
        allTreqs.append("cci")
    if eachClass.alp:
        allTreqs.append("alp")
    if eachClass.ns:
        allTreqs.append("ns")
    if eachClass.qs:
        allTreqs.append("qs")
    if eachClass.ei:
        allTreqs.append("ei")
    if eachClass.fl:
        allTreqs.append("fl")
    if eachClass.r:
        allTreqs.append("r")
    if eachClass.sts:
        allTreqs.append("sts")
    if eachClass.w:
        allTreqs.append("w")
    return allTreqs

@app.route('/get-all-majors', methods=['GET'])
def getAllMajors():
    majors = list()
    alldeps = db.session.query(models.Department).all()
    for dep in alldeps:
        majors.append(dep.department_id)
    return jsonify(majors)

def getRating(class_id):
    teachTuples = db.session.query(models.Teaches).filter(models.Teaches.class_id == class_id).all()
    totalReviews = 0
    totalScore = 0
    for teach in teachTuples:
        totalScore+=teach.average_quality*teach.num_reviews
        totalReviews+=teach.num_reviews

    return totalScore/max(totalReviews,1)

    # takenTuples = db.session.query(models.Taken).filter_by(class_id=class_id).all()
    # notNull = db.session.query(models.Taken, models.Comment).filter_by(class_id=class_id).join().all()
    # totalUpvotes = 0
    # totalDownvotes = 0
    # for comment in notNull:
    #     totalUpvotes +=comment.Comment.upvotes
    #     totalDownvotes += comment.Comment.downvotes
    # ratings = list()
    # for taken in takenTuples:
    #     if taken.comment_id is not None:
    #         #should probably optimize
    #         comment = db.session.query(models.Comment).filter_by(comment_id=taken.comment_id).first()
    #         numUpvotes = comment.upvotes
    #         numDownvotes = comment.downvotes
    #         timesToAppend = int(math.log(1/(1-numUpvotes/totalUpvotes+.00000001),2))
    #         timesToAppend -= int(math.log(1/(1-numDownvotes/totalDownvotes+.00000001),2))
    #         for i in range(timesToAppend):
    #             ratings.append(taken.star_number)
    #     ratings.append(taken.star_number)
    # total = 0
    # for rating in ratings:
    #     total+=rating
    # if len(ratings)==0:
    #     return 2.5
    # return total/len(ratings)

def getDifficulty(class_id):
    teachTuples = db.session.query(models.Teaches).filter_by(class_id=class_id).all()
    totalReviews = 0
    totalScore = 0
    for teach in teachTuples:
        totalScore+=teach.average_difficulty*teach.num_reviews
        totalReviews+=teach.num_reviews
    return totalScore/max(totalReviews,1)

def findUserMajor(user_id):
    student = db.session.query(models.Student).filter_by(student_id=user_id).first()
    return student.major

def getCompleted(user_id):
    classesTaken = db.session.query(models.Taken).filter_by(student_id=user_id).all()
    completed = dict()
    for eachClass in classesTaken:
        classItself = db.session.query(models.Class).filter_by(class_id=eachClass.class_id).first()
        if classItself.cz == 1:
            if 'cz' not in completed:
                completed['cz']=0
            completed['cz']+=1
        if classItself.ss == 1:
            if 'ss' not in completed:
                completed['ss']=0
            completed['ss']+=1
        if classItself.cci == 1:
            if 'cci' not in completed:
                completed['cci']=0
            completed['cci']+=1
        if classItself.alp == 1:
            if 'alp' not in completed:
                completed['alp']=0
            completed['alp']+=1
        if classItself.ns == 1:
            if 'ns' not in completed:
                completed['ns']=0
            completed['ns']+=1
        if classItself.qs == 1:
            if 'qs' not in completed:
                completed['qs']=0
            completed['qs']+=1
        if classItself.ei == 1:
            if 'ei' not in completed:
                completed['ei']=0
            completed['ei']+=1
        if classItself.fl == 1:
            if 'fl' not in completed:
                completed['fl']=0
            completed['fl']+=1
        if classItself.r == 1:
            if 'r' not in completed:
                completed['r']=0
            completed['r']+=1
        if classItself.sts == 1:
            if 'sts' not in completed:
                completed['sts']=0
            completed['sts']+=1
        if classItself.w == 1:
            if 'w' not in completed:
                completed['w']=0
            completed['w']+=1
    return completed

def getClassesWithReqs(needed):
    classes = dict()
    # currClasses = db.session.query(models.Class).filter(models.Class.cz==1 or models.Class.ss==1).all()
    # for currClass in currClasses:
    #     if currClass not in classes:
    #         classes[currClass] = list()
    #     if (currClass.cz == 1):
    #         classes[currClass].append('cz')
    #     if (currClass.ss == 1):
    #         classes[currClass].append('ss')
    if 'cz' in needed:
        currClasses = db.session.query(models.Class).filter_by(cz=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('cz')
    if 'ss' in needed:
        currClasses = db.session.query(models.Class).filter_by(ss=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('ss')
    if 'cci' in needed:
        currClasses = db.session.query(models.Class).filter_by(cci=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('cci')
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
    if 'qs' in needed:
        currClasses = db.session.query(models.Class).filter_by(qs=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('qs')
    if 'ei' in needed:
        currClasses = db.session.query(models.Class).filter_by(ei=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('ei')
    if 'fl' in needed:
        currClasses = db.session.query(models.Class).filter_by(fl=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('fl')
    if 'r' in needed:
        currClasses = db.session.query(models.Class).filter_by(r=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('r')
    if 'sts' in needed:
        currClasses = db.session.query(models.Class).filter_by(sts=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('sts')
    if 'w' in needed:
        currClasses = db.session.query(models.Class).filter_by(w=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('w')
    return classes


def getNeededClasses(user_id):
    completed = getCompleted(user_id)
    needed = ['cz', 'ss','cci','alp','ns','qs','ei','fl','r','sts','w']
    for key in completed:
        if completed[key]>=2:
            needed.remove(key)
    return completed, getClassesWithReqs(needed)

@app.route('/get-recommended-treqs', methods=['GET'])
def gettreqs():
    email = request.args.get('email')
    user_id = emailToId(email)
    completed, classesWithReqs = getNeededClasses(user_id)
    takenAlready = db.session.query(models.Taken).filter_by(student_id=user_id).all()
    classList = list()
    haveTaken = set()
    # similarList = dict()
    # for taken in takenAlready:
    #     haveTaken.add(taken.class_id)
    #     others = db.session.query(models.Taken).filter(models.Taken.student_id != user_id ).all()
    #     for other in others:
    #         similarList[other.student_id] += (other.star_number-3)*(taken.star_number-3)
    i = 0
    for _,eachClass in enumerate(classesWithReqs.keys()):
        if eachClass.class_id in haveTaken:
            continue
        classList.append(dict())
        classList[i]['dept'] = eachClass.department_id
        classList[i]['overall'] = round(getRating(eachClass.class_id),2)
        classList[i]['difficulty'] = round(getDifficulty(eachClass.class_id),2)
        classList[i]['name'] = eachClass.name
        classList[i]['id'] = eachClass.class_id
        classList[i]['num'] = eachClass.class_num
        classList[i]['satisfiesNeeded'] = classesWithReqs[eachClass]
        for req in classList[i]['satisfiesNeeded']:
            if 'numNeeded' not in classList[i]:
                    classList[i]['numNeeded']=dict()
            if req not in completed or completed[req]==0:
                classList[i]['numNeeded'][req] = 2
            else:
                classList[i]['numNeeded'][req]=1
        #This implements weighting by the t-reqs you need more, but would also return alp twice to the frontend if you needed two alps
        # temp = list()
        # for req in classList[i]['satisfiesNeeded']:
        #     if req not in completed or completed[req]==0:
        #         temp.append(req)
        # for t in temp:
        #     classList[i]['satisfiesNeeded'].append(t)
        i+=1
    classList = sorted(classList, key=cmp_to_key(compareClasses))
    return jsonify(classList)

def score(currClass):
    score = 0
    score += currClass['overall']
    score-=currClass['difficulty']
    if 'numNeeded' in currClass:
        for key in currClass['numNeeded'].keys():
            score+=currClass['numNeeded'][key]
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


@app.route('/get-classes-in-major', methods=['GET'])
def getClassesInMajor():
    major = request.args.get('major')
    classesInMajor = db.session.query(models.Class).filter_by(department_id=major).all()
    classList = list()
    i = 0
    for _,eachClass in enumerate(classesInMajor):
        classList.append(dict())
        classList[i]['dept'] = major
        classList[i]['overall'] = getRating(eachClass.class_id)
        classList[i]['difficulty'] = round(getDifficulty(eachClass.class_id),2)
        classList[i]['name'] = eachClass.name
        classList[i]['id'] = eachClass.class_id
        classList[i]['num'] = eachClass.class_num
        classList[i]['treqs'] = returnAllTreqs(eachClass)
        i+=1
    return jsonify(classList)

# @app.route('/get-class-info', methods=['GET'])
# def getClassInfo():
#     class_id = request.args.get('class_id')
#     return jsonify(getFullClasses()[int(class_id)])

@app.route('/get-class-info', methods=['GET'])
def getClassInfo():
    # name VARCHAR(100) NOT NULL,
    # 	class_id INTEGER NOT NULL,
    # 	department_id VARCHAR(100) NOT NULL,
    # 	class_num VARCHAR(10) NOT NULL,
    class_id = int(request.args.get('class_id'))
    classes = db.session.query(models.Class).filter_by(class_id = class_id).all()
    name = ''
    department_id = ''
    class_num = ''
    for i, eachClass in enumerate(classes):
        name = eachClass.name
        department_id = eachClass.department_id
        class_num = eachClass.class_num
    teaches = db.session.query(models.Teaches).filter_by(class_id = class_id).all()
    classList = list()
    allComments = list()
    totalOverall = 0
    totalDifficulty = 0
    totalReviews = 0
    index = 0
    for j, eachTaught in enumerate(teaches):
        classList.append(dict())
        classList[j]['quality'] = eachTaught.average_quality
        classList[j]['difficulty'] = eachTaught.average_difficulty
        classList[j]['prof_id'] = eachTaught.professor_id
        classList[j]['num_reviews'] = eachTaught.num_reviews
        classList[j]['semester'] = eachTaught.semester
        totalOverall += eachTaught.average_quality * eachTaught.num_reviews
        totalDifficulty += eachTaught.average_difficulty * eachTaught.num_reviews
        totalReviews += eachTaught.num_reviews
        profs = db.session.query(models.Professor).filter_by(professor_id = eachTaught.professor_id).all()
        profName = ''
        for k, eachProf in enumerate(profs):
            profName = eachProf.name
        classList[j]['prof_name'] = profName
        taken = db.session.query(models.Taken).filter(models.Taken.class_id == class_id).filter(models.Taken.semester == eachTaught.semester).all()
        for j, eachTaken in enumerate(taken):
            if (eachTaken.comment_id):
                comments = db.session.query(models.Comment).filter_by(comment_id = eachTaken.comment_id).all()
                for k, eachComment in enumerate(comments):
                    allComments.append({'overall': eachTaken.star_number, 'difficulty': eachTaken.difficulty,
                    'semester': eachTaught.semester, 'prof': profName,
                    'class_id': class_id, 'text': eachComment.text,
                    'up': eachComment.upvotes, 'down': eachComment.downvotes})

        j += 1
    nextSemProfs = []
    for profObj in classList:
        if (profObj['semester'] == '2019 Spring Term'):
            nextSemProfs.append(profObj)
    classList.sort(key=lambda y: y['quality'] - y['difficulty'], reverse=True)
    #classList = array of dictionaries!!! [{'prof_name': 'name', 'difficulty': 3, 'quality': 2, 'prof_id': 02313}]
    ret = []
    for dic in classList:
        ferozeName = dic['prof_name']
        for dics in ret:
            if dics['prof_name'] == ferozeName:
                # do something
                dics['difficulty'] += dic['difficulty']
                dics['quality'] += dic['quality']
                dics['count'] += 1
                break
        else:
            new_dic = {'prof_name': ferozeName, 'difficulty': dic['difficulty'], 'quality': dic['quality'], 'count': 1, 'prof_id': dic['prof_id']}
            ret.append(new_dic)
    ret2 = []
    for dic in ret:
        new_dic = {'prof_name': dic['prof_name'], 'difficulty': dic['difficulty']/dic['count'], 'quality': dic['quality']/dic['count'], 'prof_id': dic['prof_id']}
        ret2.append(new_dic)
    ret2.sort(key=lambda y: y['quality'] - y['difficulty'], reverse=True)

    overall = totalOverall / (max(totalReviews, 1))
    difficulty = totalDifficulty / (max(totalReviews, 1))

    return jsonify({'name': name, 'dept': department_id, 'class_num': class_num, 'comments': allComments,
    'semesters': classList, 'id': class_id, 'nextSemProfs': nextSemProfs, "profs": ret2,
    'overall': overall, 'difficulty': difficulty
    })
    return jsonify(ret2)




    #pro = db.session.query(models.Professor).filter_by(professor_id =id).first()
    # professors = db.session.query(models.Teaches).filter_by(professor_id = proof_id).all()
    # profList = list()
    # i = 0
    # allComments = list()
    # for _, eachProf in enumerate(professors):
    #     profList.append(dict())
    #     profList[i]['professor_id'] = eachProf.professor_id
    #     profList[i]['semester'] = eachProf.semester
    #     profList[i]['class_id'] = eachProf.class_id
    #     classes = db.session.query(models.Class).filter(models.Class.class_id == eachProf.class_id).all()
    #     for a, eachClass in enumerate(classes):
    #         profList[i]['name'] = eachClass.name
    #         profList[i]['dept'] = eachClass.department_id
    #         profList[i]['num'] = eachClass.class_num
    #     profList[i]['overall'] = eachProf.average_quality
    #     profList[i]['difficulty'] = eachProf.average_difficulty
    #     profList[i]['num_reviews'] = eachProf.num_reviews
    #     taken = db.session.query(models.Taken).filter(models.Taken.class_id == eachProf.class_id).filter(models.Taken.semester == eachProf.semester).all()
    #     top3 = list()
    #     for j, eachTaken in enumerate(taken):
    #         if (eachTaken.comment_id):
    #             print(type(eachTaken.comment_id))
    #             comments = db.session.query(models.Comment).filter_by(comment_id = eachTaken.comment_id).all()
    #             for k, eachComment in enumerate(comments):
    #                 allComments.append({'semester': eachProf.semester, 'class_id': eachProf.class_id, 'text': eachComment.text, 'up': eachComment.upvotes, 'down': eachComment.downvotes})
    #     i+=1
    # toReturn = {'name': name}
    # allComments.sort(key=lambda x: x['up'] - x['down'], reverse=True)
    # profList.sort(key=lambda y: y['overall'] - y['difficulty'], reverse=True)
    # nextSemClasses = []
    # for classObj in profList:
    #     if (classObj['semester'] == '2019 Spring Term'):
    #         nextSemClasses.append(classObj)


@app.route('/get-prof-info', methods=['GET'])
def getProfInfo():
    proof_id = int(request.args.get('prof_id'))
    professors2 = db.session.query(models.Professor).filter_by(professor_id = proof_id).all()
    name = ''
    for _, eachProf in enumerate(professors2):
        name = eachProf.name
    #pro = db.session.query(models.Professor).filter_by(professor_id =id).first()
    professors = db.session.query(models.Teaches).filter_by(professor_id = proof_id).all()
    profList = list()
    i = 0
    allComments = list()
    totalOverall = 0
    totalDifficulty = 0
    totalReviews = 0
    for _, eachProf in enumerate(professors):
        profList.append(dict())
        profList[i]['professor_id'] = eachProf.professor_id
        profList[i]['semester'] = eachProf.semester
        profList[i]['class_id'] = eachProf.class_id
        classes = db.session.query(models.Class).filter(models.Class.class_id == eachProf.class_id).all()
        for a, eachClass in enumerate(classes):
            profList[i]['name'] = eachClass.name
            profList[i]['dept'] = eachClass.department_id
            profList[i]['num'] = eachClass.class_num
            profList[i]['overall'] = eachProf.average_quality
            profList[i]['difficulty'] = eachProf.average_difficulty
            profList[i]['num_reviews'] = eachProf.num_reviews
            totalOverall += eachProf.average_quality * eachProf.num_reviews
            totalDifficulty += eachProf.average_difficulty * eachProf.num_reviews
            totalReviews += eachProf.num_reviews
            taken = db.session.query(models.Taken).filter(models.Taken.class_id == eachProf.class_id).filter(models.Taken.semester == eachProf.semester).all()
            for j, eachTaken in enumerate(taken):
                if (eachTaken.comment_id):
                    print(type(eachTaken.comment_id))
                    comments = db.session.query(models.Comment).filter_by(comment_id = eachTaken.comment_id).all()
                    for k, eachComment in enumerate(comments):
                        allComments.append({'overall': eachTaken.star_number, 'difficulty': eachTaken.difficulty,
                        'semester': eachProf.semester, 'dept': eachClass.department_id, 'num': eachClass.class_num,
                        'class_id': eachProf.class_id, 'text': eachComment.text,
                        'up': eachComment.upvotes, 'down': eachComment.downvotes})
        i+=1
    toReturn = {'name': name}
    allComments.sort(key=lambda x: x['up'] - x['down'], reverse=True)
    profList.sort(key=lambda y: y['overall'] - y['difficulty'], reverse=True)

    ret = []
    real = []

    for dic in profList:
        for dics in ret:
            if dics['extra'] == (dic['dept']+dic['num']+dic['name']):
                break
        else:
            new_dic = {'extra': (dic['dept']+dic['num']+dic['name'])}
            ret.append(new_dic)
            real.append(dic)
    profList = real
    overall = totalOverall / (max(totalReviews, 1))
    difficulty = totalDifficulty / (max(totalReviews, 1))


    nextSemClasses = []
    for classObj in profList:
        if (classObj['semester'] == '2019 Spring Term'):
            nextSemClasses.append(classObj)
    return jsonify({'name': name, 'comments': allComments, 'classes': profList,
    'prof_id': proof_id, 'nextSemClasses': nextSemClasses, 'overall': overall, 'difficulty': difficulty})

@app.route('/get-all-profs', methods=['GET'])
def getAllProfInfo():
    professors = db.session.query(models.Professor).all()
    profList = list()
    i = 0
    for _, eachProf in enumerate(professors):
        profList.append(dict())
        profList[i]['professor_id'] = eachProf.professor_id
        profList[i]['name'] = eachProf.name
        i+=1
    return jsonify(profList)

@app.route('/get-all-classes', methods=['GET'])
def getAllClasses():
    currClasses = db.session.query(models.Class).all()
    classList = list()
    haveTaken = set()
    similarList = dict()
    i = 0
    for _,eachClass in enumerate(currClasses):
        classList.append(dict())
        classList[i]['dept'] = eachClass.department_id
        classList[i]['overall'] = round(getRating(eachClass.class_id),2)
        classList[i]['difficulty'] = round(getDifficulty(eachClass.class_id),2)
        classList[i]['name'] = eachClass.name
        classList[i]['id'] = eachClass.class_id
        classList[i]['num'] = eachClass.class_num
        # cz,ss,cci,alp,ns,qs,ei,fl,r,sts,w
        classList[i]['cz'] = eachClass.cz
        classList[i]['ss'] = eachClass.ss
        classList[i]['cci'] = eachClass.cci
        classList[i]['alp'] = eachClass.alp
        classList[i]['ns'] = eachClass.ns
        classList[i]['qs'] = eachClass.qs
        classList[i]['ei'] = eachClass.ei
        classList[i]['fl'] = eachClass.fl
        classList[i]['r'] = eachClass.r
        classList[i]['sts'] = eachClass.sts
        classList[i]['w'] = eachClass.w


        i+=1
    return jsonify(classList)

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
