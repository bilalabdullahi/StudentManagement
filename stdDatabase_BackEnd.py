import sqlite3
# backend
def studentData():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, StdID text, FirstName text, \
         Surname text, DoB text, Age text, Gender text, Email text) ")
    con.commit()
    con.close()

def addStdRec(StdID, FirstName, Surname, DoB, Age, Gender, Email):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?)", (StdID, FirstName, Surname, DoB, Age, Gender, Email))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id = ?", (id,))
    con.commit()
    con.close()

def searchData(StdID = "", Firstname = "", Surname = "", DoB = "", Age = "", Gender = "", Email = "",):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM 'student' WHERE StdID = ? OR Firstname = ? OR Surname = ? OR DoB = ? OR Age = ? OR Gender= ? OR Email= ? ",
                   (StdID, Firstname, Surname, DoB, Age, Gender, Email))
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(StdID = "", Firstname = "", Surname = "", DoB = "", Age = "", Gender= "", Email= "",):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET stdID = ?, OR Firstname = ?, OR Surname = ?, OR DoB = ?, OR Age = ?, OR Gender= ?, OR Email= ? ",
                   (StdID, Firstname, Surname, DoB, Age, Gender, Email))
    con.commit()
    con.close()



studentData()