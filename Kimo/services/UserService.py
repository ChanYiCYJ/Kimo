from Kimo.models import user
from utils import hash
def login(user_noe, password):
    check_user =user.get_user_by_name_or_email(user_noe)
    if not check_user :
        return {
            "status" : 0,
            "msg" : 'User not found'
        }
    if hash.verify_password(password,check_user['password']):
        print(check_user['role'])
        if check_user['role'] == 0:
            return {
            "status" : 2,
            "msg" : 'Admin'
        }
        return {
            "status" : 1,
            "msg" : 'Password is correct'
        }
    
    return {
        "status": 0,
        "msg": 'Password is incorrect'
    }

def register(username,email,password):
    if not username or not email or not password:
        return {
        "status": False,
        "msg": '请填写必要字段'
    }
    if user.get_user_by_name(username):
        return {
        "status": False,
        "msg": '用户已存在'
    }
    if user.get_user_by_email(email):
        return {
        "status": False,
        "msg": '邮箱已存在'
    }
    result= user.insert_user_info(username,email,hash.hash_password(password))
    if not result:
        return{
        "status": False,
        "msg": '注册失败'
        }
    return {
        "status": True,
        "msg": '注册成功'
    }