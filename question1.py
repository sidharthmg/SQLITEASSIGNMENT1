import sqlite3
conn=sqlite3.connect("cars.db")
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS CARS")
query="""CREATE TABLE CARS(NAME CHAR(20),OWNER CHAR(20))"""
conn.execute(query)
cursor.execute("INSERT INTO CARS(NAME,OWNER) VALUES ('VOLKSWAGEN','JOHN'),('POLO','JAMES'),('KIA','RODRIGUEZ'),"
               "('LAMBORGINI','MATHEWS'),('MARUTI','JOSH'),('AUDI','JESSY'),('SWIFT','JOSHUA'),('WAGONR','CHARLES'),"
               "('HYUNDAI','HENDERSON'),('NISSAN','BRUCE')")
cursor=conn.execute("SELECT * FROM CARS")
print(cursor.fetchall())
conn.commit()
conn.close()