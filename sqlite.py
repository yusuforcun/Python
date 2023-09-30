import sqlite3

con = sqlite3.connect("dersler.py")

cursor = con.cursor()

def tabll():
    cursor.execute("CREATE TABLE ogrnciler(ad TEXT , num INT , nus INT)")
    con.commit()
    con.close()
    
tabll()