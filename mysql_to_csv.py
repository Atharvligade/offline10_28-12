import pymysql
import csv
def get_header():
    header = ['id', 'name', 'city']
    return header
def csv_write(filename, data):
    with open(r"{}".format(filename), "w") as fp:
        w = csv.writer(fp)
        w.writerow(get_header())
        w.writerows(data)
        return True

def fetchdb_to_csv(cur):
    cur.execute("select * from emp_grp1")
    data = cur.fetchall()
    return data
def connect2():
    conn=pymysql.connect(host="localhost",user="root",password="root",db="dbb")
    cur = conn.cursor()
    return cur

def main():
    filename='emp.csv'
    cur = connect2()
    data = fetchdb_to_csv(cur)
    status = csv_write(filename, data)
    if status:
        print("{} csv file creted successfully".format(filename))
    else:
        print("Issue in file creation")
    print("done")
if __name__=='__main__':
    main()