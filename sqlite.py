import sqlite3 as sql

def createDB():
    conn = sql.connect("digitalizacion.db")
    conn.commit()
    conn.close()
    
    
def createTable():
    conn = sql.connect("digitalizacion.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS digitalizacion (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT, dni TEXT, fecha TEXT, hora TEXT)")
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    createDB()
    createTable()
    
    

