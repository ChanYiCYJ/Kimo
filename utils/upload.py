import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER ='/file/upload'
ALLOWED_EXTENSIONS = {'jpg','jpeg','png','gif'}

def upload_file(file):
    filename=secure_filename(file)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return {
        'status':1,
        'msg':'发送成功'
    }

def delete_file():
    return 'delete file'

def get_upload_file():
    return 'file'

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
