import pymysql
from dbutils.pooled_db import PooledDB
from pymysql import cursors
from werkzeug.security import generate_password_hash, check_password_hash

from Kimo.config import load_config

dbn = 'database'
POOL = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=1,
    maxcached=1,
    maxshared=1,
    blocking=True,
    maxusage=None,
    ping=0,
    host=load_config(dbn, 'host'),
    port=load_config(dbn, 'port'),
    user=load_config(dbn, 'user'),
    password=load_config(dbn, 'password'),
    db=load_config(dbn, 'name'),
    charset=load_config(dbn, 'charset')
)



def fetch_one(sql,params):
    conn = POOL.connection()
    cursor = conn.cursor(cursor = cursors.DictCursor)
    cursor.execute(sql,params)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def register_user(sql,params):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute(sql,params)
    result = conn.commit()
    cursor.close()
    conn.close()
    return result

def fetchall(sql):
    conn = POOL.connection()
    cursor = conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def hash_password(password) -> str:
    return generate_password_hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return check_password_hash(password_hash, password)