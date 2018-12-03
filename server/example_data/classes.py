comment = {"username": "Matthew O'Boyle", "up": 7, "down": 2, "comment": "Here's a comment", 
"date": "2018-12-01", "overall": 4, "difficulty": 3.4, "grade": "B+"} 
comment2 = {"username": "Feroze", "up": 12, "down": 1, "comment": "Feroze's comment", 
"date": "2018-11-29", "overall": 3.45, "difficulty": 1.4, "grade": "A-"} 
comment3 = {"username": "Christina", "up": 1, "down": 8, "comment": "Christina's comment", 
"date": "2018-11-26", "overall": 3.7, "difficulty": 1.7, "grade": "A"} 
profs = [{"name": "Jun Yang", "id": 1, "rating": 4.7}, 
{"name": "Robert Duvall", "id": 2, "rating": 4.3}, 
{"name": "Jeff Forbes", "id": 3, "rating": 4.1}]
class1 = {"num": 316, "dept": "Compsci", "name": "Databases", "overall": 4.1, 
"difficulty": 1.2, "comments": [comment1, comment2, comment3], profs: profs, 
"nextSemProf": {"name": "Jun Yang", "id": 1, "rating": 4.7}, "recommendedSem": "Senior Fall"}

def getClasses(): 
    return class1