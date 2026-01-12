import os
from werkzeug.utils import secure_filename
from uuid import uuid4
UPLOAD_FOLDER ='Kimo/static/uploads'
ALLOWED_EXTENSIONS = {'jpg','jpeg','png','gif'}

def upload_file(file):
    if not file:
        return{
            'status':0,
            'msg':'Not file'
        }
    ext =get_file_ext(file)
    if ext not in ALLOWED_EXTENSIONS:
        return{
            'status':0,
            'msg':'不支持此文件类型'
        }
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    filename=f"{uuid4().hex}.{ext}"
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return {
        'status':1,
        'msg':'发送成功',
        "filename":filename,
        "url": f"/static/uploads/{filename}"
    }

def delete_file():
    return 'delete file'

def get_upload_file():
    return 'file'

def get_file_ext(file):
    return file.filename.rsplit(".", 1)[1].lower()
