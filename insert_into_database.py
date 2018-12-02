import random

departmentID = ["COMPSCI", "ECON", "PSYCH", "RUSSIA", "ECE", "STAT", "MATH"]

def insert_into_database(table_name):
    # @param table_name - name of the table wished to insert into
    if table_name == "Students":
        SID_array = [12341, 12234, 1292993, 19239, 12003]
        name_array = ["Suchir", "Christina", "Matt", "Salil", "Feroze"]
        email_array = ["sjdk@gmail.com", "ssld@yahoo.com", "skkd@hotmail.com"]
        ret = []
        for _ in range(10):
            ret.append("INSERT INTO Students VALUES (" + str(random.choice(SID_array)) + random.choice(name_array)
                       + random.choice(email_array))
        return ret
    elif table_name == "Taken":
        sem_array = ["F18", "S18", "F17", "S17", "F16"]
        SID_array = [12341, 12234, 1292993, 19239, 12003]
        classID_array = [1, 233, 322, 4445, 223]
        CID_array = [999292, 2939403, 202303, 303004, 23030]
        star_array = range(1,5.1,.1)
        ret = []
        ret.append("INSERT INTO Students VALUES (")
        return ret
    elif table_name == "Classes":
        classID_array = [1, 233, 322, 4445, 223]
        sem_array = ["F18", "S18", "F17", "S17", "F16"]
        name_array = ["Suchir", "Christina", "Matt", "Salil", "Feroze"]
        ret = []
        for _ in range(10):
            ret.append("INSERT INTO Students VALUES (" + str(random.choice(classID_array)) + random.choice(sem_array)
                       + random.choice(name_array))
        return ret
    elif table_name == "Teach":
        sem_array = ["F18", "S18", "F17", "S17", "F16"]
        CID_array = [999292, 2939403, 202303, 303004, 23030]
        ProfessorID_array = [23345, 23423, 23445, 2344, 532525]
        ret = []
        for _ in range(10):
            ret.append("INSERT INTO Students VALUES (" + (random.choice(sem_array)) + str(random.choice(CID_array))
                       + str(random.choice(ProfessorID_array)))
        return ret
    elif table_name == "Department":
        insertionArr = list()
        insertionArr.append("INSERT INTO Department VALUES")
        for i in range(len(departmentID)):
            if i!= len(departmentID)-1:
                insertionArr.append("('"+departmentID[i]+"',"+str(i)+"),")
            else:
                insertionArr.append("('"+departmentID[i]+"',"+str(i)+");")
        return "\n".join(insertionArr)

print(insert_into_database("Department"))