from flask import Flask,render_template , request
import sqlite3

app = Flask(__name__)

#連接資料庫的函式
def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory= sqlite3.Row # 讓查詢結果可以用欄位名稱存取
    return conn

#取得所有系所（用於下拉選單
def get_departments():
    conn =get_db_connection
    cursor =conn.cursor
    cursor.execute('SELECT DISTINCT department FROM students ORDER BY')
    departments =cursor.fetchall
    conn.close()
    return departments

def query_page():
    conn=get_db_connection()
    cursor=conn.cursor()
    students=[]
    query_type="所有學生"

    #如果是 POST 請求 使用者提交了查詢表單
    if request.method =='POST':
        action=request.form.get('action')
        #查詢功能 1 顯示所有學生
        if action=='all':
            cursor.execute('SELECT FROM students ORDER BY student_id')
            students =cursor.fetchall()
            query_type="所有學生"
        #查詢功能 2 依系所篩選
        elif action=='department':
            department=request.form.get('department')
            cursor.execute ('SELECT FROM students WHERE department ORDER BY student_id',(department,))
            students=cursor.fetchall()
            query_type=f"{department} 的學生"