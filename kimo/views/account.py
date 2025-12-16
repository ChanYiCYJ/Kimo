from flask import Blueprint, render_template, request
import pymysql
from utils import db
ac=Blueprint('account',__name__)

@ac.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')

    email=request.form.get('email')
    password=request.form.get('password')
    result=db.fetch_one('select * from userInfo where email=%s and password=%s',[email,password])
    if result:
     print(result)
     return render_template('/index.html')

    return render_template('login.html',error="请重新尝试")

@ac.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    
    # 验证输入
    if not username or not email or not password:
        return render_template('login.html', error="请填写所有必需字段")
    
    result = db.register_user('INSERT INTO userInfo(email,password,user_name) VALUES(%s,%s,%s)', [email, password, username])
    
    if result:
        return render_template('login.html', success="注册成功，请登录")
    else:
        return render_template('login.html', error="注册失败，请重试")

@ac.route('/logout')
def logout():
    return "Logout"

@ac.route('/users')
def users():
    return "Users"