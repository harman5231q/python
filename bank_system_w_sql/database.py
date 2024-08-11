import mysql.connector as sql

my_db=sql.connect(
    host="localhost",
    user="root",
    passwd="Gurne@68748",
    database="BANK"

)

cursor=my_db.cursor()

def create_table():
    cursor.execute(
    '''CREATE TABLE IF NOT EXISTS customers (
    Account_number INT PRIMARY KEY,
    NAME VARCHAR(200),
    ADDRESS VARCHAR(255),
    BALANCE INT,
    STATUS BOOLEAN
);
'''
)

def create_admin_table():
    cursor.execute(
    '''CREATE TABLE IF NOT EXISTS admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
'''
)


def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def close_con():

    cursor.close()
    my_db.close()
    
my_db.commit()

if(__name__=="__main__"):
    
    create_table()
    create_admin_table()
    # cursor.execute('''INSERT INTO admin (username, password) VALUES ('harman', '123');''')
