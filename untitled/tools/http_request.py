import requests
import json

class HttpRequest:
    def http_request(self,url,http_method,data,headers = None):
        try:
            if http_method.upper() == 'POST': # upper小写字母转为大写字母
                res = requests.post(url,json=data,headers = headers )
            elif http_method.upper() =='GET':
                res = requests.get(url,data,headers = headers)
            else:
                print("输入的请求方法不对")
        except Exception as e:
            print("请求报错了:{0}",format(e))
            raise e
        return res




if __name__ == '__main__':
    # res_url = 'https://api.apiopen.top/getSingleJoke'
    # res_data = {"sid": "28654780"}
    # res =HttpRequest().http_request(res_url,'GET',res_data)
    # print(res.json())
    #
    #
    # login_url = 'https://api.apiopen.top/getJoke'
    # login_data = {"page": 1, "count": 2, "type":"video"}
    # login_res =HttpRequest().http_request(login_url, login_data,'GET')
    # print(login_res.json())
    # recharge_url = 'https://www.3ajiepai.com/member.php?mod=logging&action=login&referer=https%3A%2F%2Fwww.3ajiepai.com%2Fforum-183-28.html'
    # recharge_data = {"mobilephone": "15096092589", "pwd": "123456"}
    # recharge_res = HttpRequest().http_tequest(login_url, login_data, 'post',login_res.cookies)
    url = 'http://online.sit.huahuihr.com/up/api/Authorization/AccountLogin'
    payload_data = { "account":'17322342002',"password":'123456'}
    login_res1 = HttpRequest().http_request(url, 'POST',payload_data)

    token = login_res1.json()['data']['accessToken']
    token = "Bearer" + " " + token
    headers = {
        "authorization": token}

    url = 'http://online.sit.huahuihr.com/eapi/api/Bank/CheckBankCard?realName'
    payload_data1 = {"realName": "%E5%BC%A0%E4%BC%9F%E4%B8%9C","idCard": "441621198604155913"}
    res = HttpRequest().http_request(url,'GET',payload_data1,headers=headers)
    print(res.json())