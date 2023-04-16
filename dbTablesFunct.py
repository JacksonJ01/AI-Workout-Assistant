from pickle import FALSE
from dbTables import dataBases
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlQuery
from PyQt5.QtCore import QDate

# creates the database###############################################################################3
def workoutDatabase():
    #connect = None
    #try:
    conn = QSqlDatabase.addDatabase("QSQLITE")
    conn.setDatabaseName("workoutDB.sqlite")
    print('connection successful'.upper())
    if not conn.open():
        print("Database Error: %s" % conn.lastError().databaseText())
    #except Error as oops:
    #    print('there has been an error:', oops)
    
    try:
        if conn.isOpen():  
            return conn
    except:
        print("Error")


def addIntoTable(conn, table: str, data: dict):
    columnName = [col for col in data]
    valueName = []

    for val in data:
        valueName.append(data[val])

    colFormat = ""
    for col in columnName:
        colFormat += f"{col}, "
    valFormat = ""
    for val in valueName:
        valFormat += f"'{val}', "
    colFormat, valFormat = colFormat[:-2], valFormat[:-2]
 
    addToTable = f"""
    INSERT INTO
        {table} 
        ({colFormat})
    VALUES
        ({valFormat})"""

    try:
        #Conn = workoutDatabase()
        if conn.isOpen():
            return QSqlQuery().exec(addToTable)
    except: 
        print("Could Not")
    finally:
        print(addToTable)


def clearTable(conn, clearPersonTable=False,
               clearExerciseTable=False, clearWorkoutDataTable=False,
               clearAll=False, clearAllPassword=None):
    tablesToClear = [
        clearPersonTable, 
        clearExerciseTable,
        clearWorkoutDataTable
        ]
         

    if True in tablesToClear or (clearAll is True and clearAllPassword == "Clear"):
        for database, clearTable in enumerate(tablesToClear):
            if clearTable is True or (clearAll is True and clearAllPassword == "Clear"):
                dropTable = f"""
                Drop Table if exists
                    {dataBases[database][1]}
                """
                try: 
                    if conn.isOpen():
                        QSqlQuery().exec(dropTable)
                except: 
                    print("Could Not")


def createTable(conn, table: str):
    try: 
        if conn.isOpen():
            QSqlQuery().exec(table)
    except:
        print("Could Not")
    print(table)


def deleteFromTable(table: str, fromWhere: dict):
    global dbConnection

    fromFormat = ""
    for col in fromWhere:
        fromFormat += f"{col} = '{fromWhere[col]}' AND "
    fromFormat = fromFormat[:-5]
    
    delFromTable = f"""
    DELETE FROM 
        {table}
    WHERE
        {fromFormat}
    """

    #try: 
    #    if dbConnection.isOpen():
    #        QSqlQuery().exec(delFromTable)
    #except: 
    #    print("Could Not")
    
    print(delFromTable)
        

def modifyTable(table: str, toSet: dict, fromWhere: dict):
    global dbConnection

    setFormat = ""
    for setCol in toSet:
        setFormat += f"{setCol} = '{toSet[setCol]}', "
    setFormat = setFormat[:-2]

    fromFormat = ""
    for col in fromWhere:
        fromFormat += f"{col} = '{fromWhere[col]}' AND "
    fromFormat = fromFormat[:-5]

    modTable = f"""
    UPDATE
        {table}
    SET
        {setFormat}
    WHERE
        {fromFormat}
    """

    #try: 
    #    if dbConnection.isOpen():
    #        QSqlQuery().exec(modTable)
    #except: 
    #    print("Could Not")
    
    print(modTable)



def selectFromTable(conn, table: str, columns=None, colNum=None, fromWhere=None):

    selFromTable: str = ""
    
    if columns is not None and fromWhere is not None:
        colFormat = ""
        for col in columns:
            colFormat += f"{col}, "
        colFormat = colFormat[:-2]

        fromFormat = ""
        for col in fromWhere:
            fromFormat += f"{col} = '{fromWhere[col]}' AND "
        fromFormat = fromFormat[:-5]

        selFromTable = f"""
            SELECT
                {colFormat}
            FROM
                {table}
            WHERE  
                {fromFormat}
        """

    elif columns is not None:
        colFormat = ""
        for col in columns:
            colFormat += f"{col}, "
        colFormat = colFormat[:-2]

        selFromTable = f"""
            SELECT
                {colFormat}
            FROM
                {table}
        """
    else:
        columns = ["val"] * colNum

        selFromTable = f"""
            SELECT
                *
            FROM
                {table}
        """

    try: 
        if conn.isOpen():
            #print(conn, table, columns, fromWhere)
            print(selFromTable)
            query = QSqlQuery(selFromTable)
            dataB = []
            while query.next():
                #print("Here2", query.value(0))
                data = []
                for val in range(0, len(columns)):
                    data.append(query.value(val))
                dataB.append(data)

            dataB_ = dataB[0][0]
            
            return dataB
    except IndexError:
        return [[False]] 


def checkReq(userInput:list, req: list = None):
    if req is None:
        num = 0
        for currentColInput in userInput:
            if currentColInput.text() != "":
                num += 1
            else:
                return False, num
    else:
        for num in req:
            if userInput[num].text() != "":
                pass
            else:
                return False, num


def checkDataType(dataType: int, data):
    try:
        if dataType == 1:
            data = int(data)
        elif 2 <= dataType <= 3:
            pass

        return True

    except ValueError:
        return data
    except TypeError:
        return data


# TEXT: 0
# INTEGER: 1
# DATE: 2
# TIME: 3
PersonData = {
    "userName": 0,
    "password": 0,
    "firstName": 0,
    "lastName": 0
}

ExerciseData = {
    "exName": 0,
    "muscleGroups": 0
 }

WorkoutData = {
    "userName": 0,
    "dateID": 2,
    "exName": 0,
    "setCount": 1,
    "repCount": 1
 }

#"""

conn = workoutDatabase()

#TESTING

#print(conn.tables())
#clearTable(conn, clearPersonTable=False, clearExerciseTable=False, clearWorkoutDataTable=False, clearAll=False)#, clearAllPassword="Clear")
#print(conn.tables())

# MOCK USER INFO
#manualCreation0 = {
#    "userName": "JJ01",
#    "password": "fitness",
#    "firstName": "Jared",
#    "lastName": "Jackson",
#    }

#manualCreation1 = {
#    "userName": "BB0",
#    "password": "abc",
#    "firstName": "Sharhea",
#    "lastName": "Wright-Havens",
#    }

#manualCreation2 = {
#    "userName": "Fit",
#    "password": "ness",
#    "firstName": "J",
#    "lastName": "J",
#    }

#createTable(conn, dataBases[0][0])
#print(conn.tables())

#addIntoTable(conn, dataBases[0][1], manualCreation0)
#addIntoTable(conn, dataBases[0][1], manualCreation1)
#addIntoTable(conn, dataBases[0][1], manualCreation2)


#columns = ["userName", "password", "firstName", "lastName"]
#fromWhere = {
#    "userName": manualCreation2["userName"]
#    }
#query: list = selectFromTable(conn, dataBases[0][1], colNum=4)
#for x in query:
#    print(x)


# EXERCISE INFO

#exercise0 = {
#    "exName": "abductorLegRaises", 
#    "muscleGroups": "Biceps"
#    }

#exercise1 = {
#    "exName": "barbellSquats", 
#    "muscleGroups": "Quads | Glutes | Lower Back"
#    }

#exercise2 = {
#    "exName": "bicepCurls", 
#    "muscleGroups": "Biceps"
#    }


#exercise3 = {
#    "exName": "singleArmBicepCurls", 
#    "muscleGroups": "Biceps"
#    }


#exercise4 = {
#    "exName": "deltoidArmRaises", 
#    "muscleGroups": "Deltoids | Traps"
#    }


#exercise5 = {
#    "exName": "singleArmDeltoidRaises", 
#    "muscleGroups": "Deltoids | Traps"
#    }


#exercise6 = {
#    "exName": "frontLatRaises",
#    "muscleGroups": "Deltoids | Traps | Lats"
#    }


#exercise7 = {
#    "exName": "singleFrontLatRaises", 
#    "muscleGroups": "Deltoids | Traps | Lats"
#    }

#exercise8 = {
#    "exName": "gobletSquats", 
#    "muscleGroups": "Quads | Calves | Glutes | Arms | Lower Back | Grip Strength"
#    }


#exercise9 = {
#    "exName": "shoulderPress", 
#    "muscleGroups": "Deltoids | Traps | Triceps | Chest"
#    }

#exercise10 = {
#    "exName": "singleArmShoulderPress", 
#    "muscleGroups": "Deltoids | Traps | Triceps | Chest"
#    }

#createTable(conn, dataBases[1][0])
#print(conn.tables())
#print(addIntoTable(conn, dataBases[1][1], exercise0))
#addIntoTable(conn, dataBases[1][1], exercise1)
#addIntoTable(conn, dataBases[1][1], exercise2)
#addIntoTable(conn, dataBases[1][1], exercise3)
#addIntoTable(conn, dataBases[1][1], exercise4)
#addIntoTable(conn, dataBases[1][1], exercise5)
#addIntoTable(conn, dataBases[1][1], exercise6)
#addIntoTable(conn, dataBases[1][1], exercise7)
#addIntoTable(conn, dataBases[1][1], exercise8)
#addIntoTable(conn, dataBases[1][1], exercise9)
#addIntoTable(conn, dataBases[1][1], exercise10)

#columns = ["exName", "muscleGroups"]
#fromWhere = {
#    "": 
#    }


#query: list = selectFromTable(conn, dataBases[1][1], colNum=2)
#for x in query:
#    print(x)


### 
#print(QDate().currentDate().toString("yyyy:MM:dd"))
#WorkoutDataDicts = {
#    "userName": "Fit",
#    "dateID": QDate().currentDate().toString("yyyy:MM:dd"),
#    "exName": "bicepCurls",
#    "setCount": 4,
#    "repCount": 10
# }

#clearTable(conn, clearPersonTable=False, clearExerciseTable=False, clearWorkoutDataTable=True, clearAll=False)#, clearAllPassword="Clear")
#createTable(conn, dataBases[2][0])
#print(conn.tables()) 
#addIntoTable(conn, dataBases[2][1], WorkoutDataDicts)


#columns = []
#fromWhere = {
#    "": 
#    }


#query: list = selectFromTable(conn, dataBases[2][1], colNum=6)
#for x in query:
#    print(x)

#input()
#"""