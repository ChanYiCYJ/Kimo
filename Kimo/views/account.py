from flask import Blueprint, render_template, request, redirect, url_for, session

from Kimo.config import load_config
from utils import db
from utils.db import hash_password

ac=Blueprint('account',__name__)
@ac.route('/login',methods=['GET','POST'])
def login():
    config = load_config('app', 'config')
    if request.method=='GET':
        return render_template('login.html', config=config)

    user_info = request.form.get('userInfo')
    password=request.form.get('password')
    result=db.fetch_one('select * from userInfo where email=%s or user_name=%s',[user_info,user_info])
    if result and db.verify_password(password,result['password']):
     print(result)
     session['user_role']=result['role']
     if result['role'] == 1:
         print(user_info, '子用户登录')
         return redirect(url_for('archive.index'))

     print(user_info, '管理员登录')
     return redirect(url_for('account.dashboard'))

    return render_template('login.html', modal="请重新尝试")

@ac.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    
    # 验证输入
    if not username or not email or not password:
        return render_template('login.html', modal="请填写所有必需字段")
    check = db.fetch_one('select * from userInfo where email=%s or user_name=%s', [email, username])
    print(check)
    if check:
        return render_template('login.html', modal="用户已存在，请重新注册")

    hash_prd = hash_password(password)
    db.increase('INSERT INTO userInfo(email,password,user_name) VALUES(%s,%s,%s)',
                [email, hash_prd, username])
    return render_template('login.html', modal="注册成功，请登录")

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
        check_user = session.get('user_role')

        if check_user == 0:
            return render_template('dashboard.html')

        print(check_user)
    return redirect(url_for('account.login'))
