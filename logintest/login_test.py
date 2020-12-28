import requests
import yaml
from getdata import Getdata


class Testlogin():
    data = Getdata()
    username = data.getdata('data', 'username')
    pwd = data.getdata('data', 'password')
    address = data.getdata('data', 'address')




    def test_login(self, username=username, pwd=pwd, address=address):
        url = f"{address}/api/Access/Login"
        payload = f'userName={username}&userPwd={pwd}'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url, headers=headers, data=payload)
        print(response.json())
        t = response.json()['result']['token']
        # token = {'token': t}
        self.data.send_token('token','token',t)
        assert response.status_code == 200


    def test_loginout(self):
        url = f"{self.address}/api/Access/LogOut"
        response = requests.request("GET", url)
        assert response.status_code == 200
