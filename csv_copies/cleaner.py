filename = "sqlFiles/class.sql"
filout = "classescleaned.sql"

with open(filename) as filein:
    with open(filout,"w") as fileo:
        for line in filein.readlines():
            lineSplit = line.split(",")
            if len(lineSplit)>1:
                print(lineSplit[2])
            try:
                int(lineSplit[2][1:-1])
                if len(lineSplit)==16:
                    fileo.write(line)
            except:
                print("nice")