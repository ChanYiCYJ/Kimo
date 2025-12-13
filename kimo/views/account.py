from flask import Blueprint, render_template, request,jsonify
import pymysql
ac=Blueprint('account',__name__)

@ac.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')

    email=request.form.get('email')
    password=request.form.get('password')
    conn =pymysql.connect(host='127.0.0.1',port=3306,user='root',password='a3022535842',db='kimoServer',charset='utf8')
    cursor=conn.cursor()
    cursor.execute('select * from userInfo where email=%s and password=%s',[email,password])
    user_dict=cursor.fetchone()
    print(user_dict)
    cursor.close()
    conn.close()
    if user_dict:
     return render_template('/index.html')

    return render_template('login.html',error="请重新尝试")

@ac.route('/register')
def register():
    return "Register"

@ac.route('/logout')
def logout():
    return "Logout"

@ac.route('/users')
def users():
    return "Users"