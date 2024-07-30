# Importing sqlite3 module
import sqlite3

# Connect to the database (create if it doesn't exist) and create table.
# Then commits changes and closes connection to db.
conn = sqlite3.connect('databaseAssignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_documents( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files STRING \
        )")
    conn.commit()
conn.close()


# Reconnect to the database and insert file names into table.
# Then commits changes and closes connection to db.
conn = sqlite3.connect('databaseAssignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_documents(col_files) VALUES (?)", \
                ('information.docx',))
    cur.execute("INSERT INTO tbl_documents(col_files) VALUES (?)", \
                ('Hello.txt',))
    cur.execute("INSERT INTO tbl_documents(col_files) VALUES (?)", \
                ('myImage.png',))
    cur.execute("INSERT INTO tbl_documents(col_files) VALUES (?)", \
                ('myMovie.mpg',))
    cur.execute("INSERT INTO tbl_documents(col_files) VALUES (?)", \
                ('World.txt',))
    cur.execute("INSERT INTO tbl_documents(col_files) VALUES (?)", \
                ('data.pdf',))
    cur.execute("INSERT INTO tbl_documents(col_files) VALUES (?)", \
                ('myPhoto.jpg',))
    conn.commit()
conn.close()


# Reconnect to the database and fetch .txt files. Prints them to console.
# Then closes connection to db.
conn = sqlite3.connect('databaseAssignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_files FROM tbl_documents WHERE col_files LIKE '%.txt'")
    txt_files = cur.fetchall()
    for file in txt_files:
        print(file[0])
conn.close
