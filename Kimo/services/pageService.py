from models import page 

def create(name,type,content):
    if type == 'markdown':
        return 'markdown_page'
    else:
        return 'html_page'

def edit(name,type,content):
    if type == 'markdown':
        return 'markdown_page'
    else:
        return 'html_page'

def delete(id):
    result=page.delete_page(id)
    if result:
        return 'sucess'
    return 'failed'

def get(name):
    id = page.get_page(name)