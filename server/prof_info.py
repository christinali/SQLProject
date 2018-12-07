class1 = {"id": "0", "name": "Compsci316 - Databases"}

class2 = {"id": "1", "name": "Compsci201 - Algorithms"}

comment1 = {"id": "0", "username": "Matthew O'Boyle", "up": 7, "down": 2, "comment": "Here's a comment", 
"date": "2018-12-01", "overall": 4, "difficulty": 3.4, "grade": "B+"} 
comment2 = {"id": "1", "username": "Feroze", "up": 12, "down": 1, "comment": "Feroze's comment", 
"date": "2018-11-29", "overall": 3.45, "difficulty": 1.4, "grade": "A-"} 
comment3 = {"id": "2", "username": "Christina", "up": 1, "down": 8, "comment": "Christina's comment", 
"date": "2018-11-26", "overall": 3.7, "difficulty": 1.7, "grade": "A"} 
comment4 = {"id": "3", "username": "Salil", "up": 47, "down": 3, "comment": "Salil's comment", 
"date": "2018-11-21", "overall": 3.2, "difficulty": 3.45, "grade": "B-"} 


jun = {"name": "Jun Yang", "id": 1, "overall": 4.7, "difficulty": 2.1, "nextSemClasses": [class1],
"topComments": [comment1, comment2, comment3]}
rob = {"name": "Robert Duvall", "id": 2, "overall": 4.3, "difficulty": 2.9, "nextSemClasses": [class2], 
"topComments": [comment3, comment2, comment4]}
jeff = {"name": "Jeff Forbes", "id": 3, "overall": 4.1, "difficulty": 4.1, "nextSemClasses": [class1, class2],
"topComments": [comment1, comment3, comment2]}
susan = {"name": "Susan Rodger", "id": 4, "overall": 2.1, "difficulty": 1.1, "nextSemClasses": [class1, class2],
"topComments": [comment3, comment2, comment4]}
astrachan = {"name": "Astrachan", "id": 5, "overall": 1.2, "difficulty": 4.5, "nextSemClasses": [],
"topComments": [comment2, comment1, comment4]}

def getAllProfs(): 
    return [jun, rob, jeff, susan, astrachan]