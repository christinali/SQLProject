filename = "classes.csv"
filout = "classescleaned.csv"

with open(filename) as filein:
    with open(filout,"w") as fileo:
        for line in filein.readlines():
            lineSplit = line.split(",")
            # if len(lineSplit)>1:
            #     print(lineSplit[2])
            # try:
            #     int(lineSplit[2][1:-1])
            #     if len(lineSplit)==16:
            #         fileo.write(line)
            # except:
            #     print("nice")
            while len(lineSplit)!=15:
                lineSplit[1] = lineSplit[0]+lineSplit[1]
                lineSplit = lineSplit[1:]
            fileo.write(",".join(lineSplit))