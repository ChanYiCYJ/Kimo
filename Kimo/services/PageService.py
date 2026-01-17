from Kimo.models import page
import json
support_type={'markdown','html','list'}
def create(name,page_type,content):
    check =page.get_page_by_name(name)
    if check:
        return {
            'status': False,
            'msg': '创建Page时不可重名'
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
            'msg':'Page成功'
        }
    return {
        'status': False,
        'msg':'创建失败'
    }


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
    return content

def get_page_html(content):
    return content

def get_page_list(content):
    lists = json.loads(content)
    return lists
