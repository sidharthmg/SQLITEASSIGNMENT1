import sqlite3
conn=sqlite3.connect("hospital.db")
conn=sqlite3.connect("doctor.db")
cursor=conn.cursor()
query="""CREATE TABLE HOSPITAL(HOSPITAL_ID INT NOT NULL PRIMARY KEY,HOSPITAL_NAME CHAR(20),BED_COUNT INT)"""
cursor.execute("INSERT INTO HOSPITAL(HOSPITAL_ID,HOSPITAL_NAME,BED_COUNT) VALUES (1,'MAYO CLINIC',200),(2,'CLEVELAND CLINIC',400),"
               "(3,'JOHNS HOPKINS',1000),(4,'UCLA MEDICAL CENTER',1500)")
query1="""CREATE TABLE DOCTOR(DOCTOR_ID INT NOT NULL PRIMARY KEY,DOCTOR_NAME CHAR(20),HOSPITAL_ID INT,JOINING_DATE DATE,
          SPECIALITY CHAR(20),SALARY INT,EXPERIENCE CHAR(20),FOREIGN KEY(HOSPITAL_ID) REFERENCES HOSPITAL(HOSPITAL_ID))"""
conn.execute(query1)
cursor.execute ("INSERT INTO DOCTOR(DOCTOR_ID,DOCTOR_NAME,HOSPITAL_ID,JOINING_DATE,SPECIALITY,SALARY,EXPERIENCE)"
               "VALUES (101,'DAVID',1,'2005-20-10','PEDIATRIC',40000,'NULL'),"
               "(102,'MICHAEL',1,'2018-07-23','ONCOLOGIST',20000,'NULL'),"
               "(103,'SUSAN',1,'2016-05-19','GAMACOLOGIST',25000,'NULL'),"
               "(104,'ROBERT',2,'2017-12-28','PEDIATRIC',28000,'NULL')"
               "(105,'LINDA',3,'2004-06-24','GAMACOLOGIST',42000,'NULL')"
               "(106,'WILLIAM',3,'2012-09-11',DERMATOLOGIST',30000,'NULL')"
               "(107,'RICHARD',4,'2014-08-21','GAMACOLOGIST',32000,'NULL')"
               "(108,'KAREN',4,'2011-10-17',RADIOLOGIST,3000,NULL")

def getdoctorlist_speciality(speciality,salary):
    sql_select_query = "SELECT * from DOCTOR where speciality = ? and salary > ?"
    cursor.execute(sql_select_query, (speciality, salary))
    records = cursor.fetchall()
    print("Printing doctors whose specialty is", speciality, "and salary greater than", salary, "\n")
    for row in records:
        print("Doctor Id: ", row[0])
        print("Doctor Name:", row[1])
        print("Hospital Id:", row[2])
        print("Joining Date:", row[3])
        print("Specialty:", row[4])
        print("Salary:", row[5])
        print("Experience:", row[6], "\n")


def get_hospital_name(hospital_id):
       select_query = "SELECT * from HOSPITAL where Hospital_Id = ?"
       cursor.execute(select_query, (hospital_id,))
       record = cursor.fetchone()
       return record[1]

def get_doctors(hospital_id):
        hospital_name = get_hospital_name(hospital_id)
        sql_select_query = "SELECT* from DOCTOR where Hospital_Id = ?"""
        cursor.execute(sql_select_query, (hospital_id,))
        records = cursor.fetchall()

        print("Printing Doctors of ", hospital_name, "Hospital")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Hospital Name:", hospital_name)
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")

speciality =input("\n Enter the speciality in which the list of doctors have to be found out")
salary=input("\n Enter the salary above which the list of doctors in this speciality have to be found out")
getdoctorlist_speciality(speciality,salary)
hospital_id=input("\n Enter the hospital id for which all the doctors have to be listed")
get_hospital_name(hospital_id)
get_doctors(hospital_id)
conn.commit()
conn.close()


