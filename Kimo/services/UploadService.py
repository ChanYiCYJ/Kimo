from utils import upload
SENDIMAGETYPE =['image','vditorImage']
def sendImage(file,type):
    result=upload.upload_file(file)
    if not result['status']:
        return {
            "status"
        }
    return 'sendImage'

def image_typeChecker(type):
    if type not in SENDIMAGETYPE:
        return{
            "status":0,
            "msg":'这是未知发送图片的方式'
        }
    if type =='image':
        return 
    
def vditor_result(status,msg:str):
    if not status:
        return {
            "code":1,
            "msg":msg
        }
    return {
        "code":0,
        "msg":msg
    }