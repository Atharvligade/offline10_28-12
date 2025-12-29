import pymysql
import json

def connect_mysql():
    conn=pymysql.connect(host='localhost',user='root',password='root',db='dbb')
    cur=conn.cursor()
    return conn,cur

def fetch_data_json():
#this is demo for gitbranch review and merging