from flask import Blueprint, render_template, request, redirect, url_for, session

from utils import db
from utils.db import hash_password

ac=Blueprint('account',__name__)
@ac.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')

    user_info=request.form.get('email')
    password=request.form.get('password')
    result=db.fetch_one('select * from userInfo where email=%s or user_name=%s',[user_info,user_info])
    if result and db.verify_password(password,result['password']):
     print(result)
     session['user_role']=result['role']
     return redirect(url_for('archive.index'))

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

    hashword = hash_password(password)
    result = db.register_user('INSERT INTO userInfo(email,password,user_name) VALUES(%s,%s,%s)', [email, hashword, username])

    if result:
        return render_template('login.html', success="注册成功，请登录")
    else:
        return render_template('login.html', error="注册失败，请重试")

@ac.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))

@ac.route('/users')
def users():
    return "Users"

@ac.route('/dashboard')
def dashboard():
    if request.method=='GET':
        return render_template('dashboard.html')
    return render_template('/dashboard.html')
