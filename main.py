import pymysql

def connect1():
    conn=pymysql.connect(
    host='localhost', port=3306, user='root', password='root',database='dbb')
    cur = conn.cursor()
    cur.execute("select * from emp_grp1")
    show=cur.fetchall()
    print(show)
    cur.close()

connect1()


def add():
    pass
def sub():
    pass


