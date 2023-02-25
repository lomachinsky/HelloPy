import http.client
import json


def get_ini():

    with open('ini.json') as f:
        file_content = f.read()
        templates = json.loads(file_content)

    return templates


def get_supp_ticket():

    ini_content = get_ini().get('supp')

    conn = http.client.HTTPSConnection(ini_content.get('url'))
    payload = json.dumps({
        "getTicket": 1000
    })
    headers = {
        'Authorization': 'Bearer '+ini_content.get('bearer'),
        'Content-Type': 'application/json',
        'Cookie': ini_content.get('cookie')
    }
    conn.request("GET", "/api/supp/", payload, headers)
    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")
