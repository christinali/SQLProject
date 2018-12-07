jun = {"name": "Jun Yang", "id": 1, "rating": 4.7}
rob = {"name": "Robert Duvall", "id": 2, "rating": 4.3}
jeff = {"name": "Jeff Forbes", "id": 3, "rating": 4.1}
susan = {"name": "Susan Rodger", "id": 4, "rating": 2.1}
astrachan = {"name": "Astrachan", "id": 5, "rating": 1.2}
amy = {"name": "Amy Anderson", "id": 6, "rating": 4.7}
orin = {"name": "Orin Starn", "id": 7, "rating": 2.1}

class1 = {"id": "0", "num": 316, "dept": "Compsci", "name": "Databases", "overall": 4.1, 
"difficulty": 1.2, "nextSemProf": jun}

class2 = {"id": "1", "num": 201, "dept": "Compsci", "name": "Algorithms", "overall": 3.7, 
"difficulty": 4.5, "nextSemProf": jeff}

class3 = {"id": "2", "num": 250, "dept": "Compsci", "name": "Computer Architecture", "overall": 2.1, 
"difficulty": 4.9, "nextSemProf": rob}

class4 = {"id": "4", "num": 101, "dept": "Compsci", "name": "Python", "overall": 4.9, 
"difficulty": 2.3, "nextSemProf": susan}

class5 = {"id": "5", "num": 101, "dept": "CulAnth", "name": "Cultural Anthropology", "overall": 3.2, 
"difficulty": 3.1, "nextSemProf": orin}

class6 = {"id": "6", "num": 101, "dept": "Educ", "name": "Foundations of Education", "overall": 4.3, 
"difficulty": 3.6, "nextSemProf": amy}

def getMajors():
    return [class1, class2, class3]
    
def getTreqs(): 
    return [class5, class4, class6]