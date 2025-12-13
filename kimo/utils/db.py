import pymysql
from flask import Flask, render_template, request, jsonify, session
from dbutils.pooled_db import PooledDB
POOL = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=1,
    maxcached=1,
    maxshared=1,
    blocking=True,
    maxusage=None,
    ping=0,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='a3022535842',
    db='kimoServer',
    charset='utf8'

)