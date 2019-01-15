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
    pprint.pprint(retobj)
    return retobj

ret1 = list_course()
addret = add_course('ruby','ruby_desc',2)

assert addret['retcode'] == 2
ret2 = list_course()

assert ret1 == ret2

print("符合预期")
