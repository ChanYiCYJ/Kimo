from Kimo.models import page
import json
from Kimo.services import ArticlesService
support_type={'markdown','html','list'}
def create(name,content,page_type):
    check =page.get_page_by_name(name)
    if check:
        return {
            'status': False,
            'msg': '创建Page时不可重名'
        }
    if not content:
        return {
            'status': False,
            'msg':'You need to enter content'
        }
    if not page_type:
        return {
            'status': False,
            'msg':'You need to enter page type'
        }
    if page_type not in support_type:
        return {
            'status': False,
            'msg':'Page不支持该格式'
        }
    result =page.create_page(name,content,page_type)
    if result['status']:
        return {
            'status': True,
            'msg':'Created Page'
        }
    return {
        'status': False,
        'msg':'创建失败'
    }

def edit(page_id,name,content,page_type):
    check =page.get_page_by_id(page_id)
    if not check:
        return {
            'status': False,
            'msg':'Not have this page'
        }
    if not name:
        return {
            'status': False,
            'msg':'You need to enter name'
        }
    if not content:
        return {
            'status': False,
            'msg':'You need to enter content'
        }
    if not page_type:
        return {
            'status': False,
            'msg':'You need to enter page type'
        }
    result =page.edit_page(page_id,name,content,page_type)
    if result:
        return {

            'status': True,
            'msg':'Edited Page'
        }
    return {
        'status': False,
        'mag':'Failed'
    }

def get_all_page():
    result =page.get_all_page()
    print(result)
    return result

def get_by_id(page_id):
    return page.get_page_by_id(page_id)

def get_by_name(page_name):
    page_result = page.get_page_by_name(page_name)
    if page_result:
        if page_result['type']=='list':
            content = get_page_list(page_result['content'])
            return {
                'status': True,
                'msg': '查询成功',
                'page_name': page_result['name'],
                'page_type': page_result['type'],
                'content': content
            }
        if page_result['type']=='markdown':
            content = get_page_markdown(page_result['content'])
            return {
                'status': True,
                'msg': '查询成功',
                'page_name': page_result['name'],
                'page_type': page_result['type'],
                'content': content
            }
        return {
            'status': True,
            'msg': '查询成功',
            'page_name': page_result['name'],
            'page_type': page_result['type'],
            'content': page_result['content']
        }
    return {
        'status': False,
        'msg':'查询出错'
    }
def get_page_markdown(content):
    return ArticlesService.switch_markdown_to_html(content)



def get_page_list(content):
    lists = json.loads(content)
    return lists
