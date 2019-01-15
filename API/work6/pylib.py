import requests
import pprint


def add_course(name,desc,display_idx):
    payload = {
        'action': 'add_course',
        'data': f'''{{
         "name":"{name}",
         "desc":"{desc}",
         "display_idx":"{display_idx}"
         }}'''
    }

    r = requests.post("http://localhost/api/mgr/sq_mgr/",
                      data=payload)
    retobj = r.json()
    pprint.pprint(retobj)
    return retobj


def list_course():
    r = requests.get("http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")
    retobj = r.json()
    pprint.pprint(retobj)
    return retobj


def modify_course(cid,name,desc,idx):
    payload = {
        'action': 'modify_course',
        'id': cid,
        'newdata': ''' {
            "name":"%s",
            "desc":"%s",
            "display_idx":"%s
        }''' % (name,desc,idx)
    }

    r = requests.put("http://localhost/api/mgr/sq_mgr/",
                      data=payload)
    retobj = r.json()
    pprint.pprint(retobj)
    return retobj


def delete_course(cid):
    payload = {
        'action': 'delete_course',
        'id': cid
    }

    r = requests.delete("http://localhost/api/mgr/sq_mgr/",
                      data=payload)
    retobj = r.json()
    pprint.pprint(retobj)
    return retobj



c1 = list_course()['retlist']
for one in c1:
    if one['name'] == 'python':
        delete_course(one['id'])


add_course('python','python语言','1')

c2 = list_course()['retlist']
for one in c2:
    if one['name'] == 'python':
        c2id = one['id']
print(c2id)
modify_course(c2id,'new_python','python_desc','2')

# assert ret['retcode'] == 0



