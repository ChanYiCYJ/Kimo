import pymysql
from dbutils.pooled_db import PooledDB
from pymysql import cursors
from werkzeug.security import generate_password_hash, check_password_hash

from Kimo.config import load_config

_db_pool = None


def init_db_pool():
    global _db_pool
    if _db_pool is not None:
        return _db_pool

    try:
        _db_pool = PooledDB(
            creator=pymysql,
            maxconnections=10,
            blocking=True,
            host=load_config('database', 'host'),
            port=load_config('database', 'port'),
            user=load_config('database', 'user'),
            password=load_config('database', 'password'),
            db=load_config('database', 'name'),
            charset=load_config('database', 'charset'),
        )
        return _db_pool
    except Exception as e:
        print("数据库初始化失败:", e)
        _db_pool = None
        return None


def get_db_connection():
    pool = init_db_pool()
    if not pool:
        return None

    try:
        return pool.connection()
    except Exception as e:
        print("数据库连接失败:", e)
        return None

def fetchall(sql, params=None):
    conn = get_db_connection()
    if not conn:
        return []

    cursor = conn.cursor(cursor=cursors.DictCursor)
    try:
        cursor.execute(sql, params or ())
        return cursor.fetchall()
    except Exception as e:
        print("SQL 执行失败:", e)
        return []
    finally:
        cursor.close()
        conn.close()


def implement(sql, params=None):
    conn = get_db_connection()
    if not conn:
        return False

    cursor = conn.cursor()
    try:
        cursor.execute(sql, params or ())
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print("SQL 执行失败:", e)
        return False
    finally:
        cursor.close()
        conn.close()

def fetch_one(sql, params=None):
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor(cursor=cursors.DictCursor)
    try:
        cursor.execute(sql, params or ())
        return cursor.fetchone()
    except Exception as e:
        print("SQL 执行失败:", e)
        return None
    finally:
        cursor.close()
        conn.close()


def hash_password(password) -> str:
    return generate_password_hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return check_password_hash(password_hash, password)