import requests


class GetToken():
    def token(self):
        url = 'http://online.sit.huahuihr.com/up/api/Authorization/AccountLogin'
        payload = {
             "account":'13530473708',
             "password":'123456'
        }
        res= requests.post(url,json=payload)
        token = res.json()['data']['accessToken']
        token = "Bearer" + " " + token
        headers = {
            "authorization": token}
        return headers


    def checkbank(self):
        url = 'http://online.sit.huahuihr.com/eapi/api/Bank/CheckIdCard'
        payload_data1 = {"realName": "张伟东", "idCard": "441621198604155913"}
        res = requests.get(url,payload_data1,headers=GetToken().token())
        print(res.json())

GetToken().checkbank()