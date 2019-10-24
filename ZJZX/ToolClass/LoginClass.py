#本用例用于系统登录
import requests
class LoginClass:
    def login(self, url, username, password):
        head = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        payload = {
            "UserName": username,
            "Password": password,
            "ReturnUrl": ""
        }
        #使用requests.session()获得session，后续请求使用session.post()等，可保持登录状态
        session=requests.session()
        response = session.post(url + "/Systems/Home/LogOn", headers=head, data=payload)
        return response.status_code,session