import requests
import pprint

def list_course():
    p = {
        'action': 'list_course',
        'pagenum': 1,
        'pagesize': 20
    }

    r = requests.get("http://localhost/api/mgr/sq_mgr/",
                     params=p)
    retobj = r.json()
    return retobj

def add_course(name,desc,idx):
    payload = {
        'action': 'add_course',
        'data': '''{
            "name":"%s",
            "desc":"%s",
            "display_idx":"%s"        
        }''' %(name,desc,idx)
    }

    r = requests.post("http://localhost/api/mgr/sq_mgr/",
                      data=payload)
    retobj = r.json()
    return retobj

ret1 = list_course()
addret = add_course('ruby','ruby_desc',2)


assert addret['retcode'] == 0

ret2 = list_course()

newcourse = None
for course in ret2['retlist']:
    if course not in ret1['retlist']:
        newcourse = course

pprint.pprint(newcourse)


assert newcourse == {'desc': 'ruby_desc', 'display_idx': 2, 'id':newcourse['id'], 'name': 'ruby'}
print('与预期相符')
