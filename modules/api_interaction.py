import http.client
import json


def get_supp_ticket():

    conn = http.client.HTTPSConnection("portal.ctrs.com.ua")
    payload = json.dumps({
        "getTicket": 1000
    })
    headers = {
        'Authorization': 'Bearer rkv2TSLP71ac9295bb300468d3880aa9f1a09736',
        'Content-Type': 'application/json',
        'Cookie': 'BITRIX_SM_GUEST_ID=427533; BITRIX_SM_LAST_VISIT=23.02.2023%2017%3A58%3A37; PHPSESSID=GwkQDoIPyq6TxieIvI1e5IHRX7VTXw2K'
    }
    conn.request("GET", "/api/supp/", payload, headers)
    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")
