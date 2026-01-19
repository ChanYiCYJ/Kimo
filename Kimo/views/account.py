from flask import Blueprint, render_template, request, redirect, url_for, session
from Kimo.services import UserService
ac=Blueprint('account',__name__)
@ac.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    result = UserService.login(
        request.form.get('userInfo'),request.form.get('password'))
    if not result["status"]:
        print(result['msg'])
        return render_template('login.html', modal=result['msg'])
    
    if result['status'] == 2:
        session['user_role']=result['status']
        return redirect(url_for("dashboard.index"))
    print(result['msg'])
    return redirect(url_for("article.index"))

@ac.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return redirect(url_for("account.login"))
    result = UserService.register(username = request.form.get('username'),
    email = request.form.get('email'),
    password = request.form.get('password')
    )
    if not result["status"]:
        print(result['msg'])
        return render_template('login.html', modal=result['msg'])
    
    return render_template('login.html', modal="注册成功，请登录")

@ac.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("account.login"))

@ac.route('/users')
def users():
    return "Users"

