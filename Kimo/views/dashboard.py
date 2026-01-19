from flask import Blueprint, render_template, request, session, jsonify,redirect,url_for

ds=Blueprint('dashboard',__name__)

ds.route('/dashboard',methods=['GET'])
def dashboard():
    return 'dashboard'

ds.route('/dashboard/pages',methods=['GET'])
def pages_manage():
    return 'aaaa'