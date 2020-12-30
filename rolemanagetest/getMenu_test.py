import pytest
import requests

from getdata import Getdata


class TestGetmenu:
    def setup(self):
        self.data = Getdata()
        self.token = self.data.getdata('token', 'token')
        self.address = self.data.getdata('data', 'address')
        #self.areaid=self.data.getdata('areaid','area_id')

    # 获取所有已交付地点area_id
    def test_getarea_id(self):
        url = f"{self.address}/api/BasicData/getAllDeliveryAreas"
        payload = {}
        headers = {'X-Token': f'{self.token}','Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("GET", url, headers=headers, data=payload)
        id = response.json()['result']['data']
        ids = []
        for i in range(len(id)):
            areaid = id[i]['id']
            ids.append(areaid)
        self.data.send_data('areaid', 'area_id', ids)
        print(response.json())
        assert response.status_code == 200
    #根据id获取酒店名称
    def getarea_name(self,areaid):
        url = f"{self.address}/api/cloud/Areas/getAreaInfo"
        payload = f'area_id={areaid}'
        headers = {'X-Token': f'{self.token}', 'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()['result']['data']['basic']['area_name']
    # 根据id获取当天明细报表任务
    # areaid = Getdata.getdata('areaid', 'area_id')
    @pytest.mark.parametrize('areaid', Getdata.getdata('','areaid','area_id'))
    def test_getdetail(self, areaid):
        begindate = "2020-12-25"
        enddate = "2020-12-29"
        url = f"{self.address}/api/cloud/RunLog/getDetailRunLogs"
        payload = f'begin_date={begindate}&end_date={enddate}&area_id={areaid}'
        headers = {'X-Token': f'{self.token}','Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.json())
        #统计任务类型
        if(len(response.json()['result']['data']) <= 0):
            print(f"{self.getarea_name(areaid)}在{begindate}号到{enddate}号没有任务")
        assert response.status_code == 200
        assert response.json()['result']['data'] != 0
    #判断明细报表中所有已交付地点都有数据


    @pytest.mark.parametrize('areaid', Getdata.getdata('', 'areaid', 'area_id'))
    def test_getalldetail(self, areaid):
        begindate = "2020-12-29"
        enddate = "2020-12-29"
        url = f"{self.address}/api/cloud/RunLog/getDetailRunLogs"
        payload = f'begin_date={begindate}&end_date={enddate}&area_id={areaid}'
        headers = {'X-Token': f'{self.token}', 'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.json())
        data=response.json()['result']['data']
        # 统计任务类型
        if (len(data) <= 0):
            print(f"{self.getarea_name(areaid)}在{begindate}到{enddate}期间没有任务")
        else:
            map={}
            result={}
            for i in range(len(data)):
                item=data[i]
                key=item['run_type']
                if(map.get(key)):
                    map[key]+=1
                else:
                    map[key]=1
            for i in range(len(data)):
                item = data[i]
                key = item['run_result']
                if (result.get(key)):
                    result[key] += 1
                else:
                    result[key] = 1
        print(f'任务类型:数量:{map},任务状态:数量:{result}')
        assert response.status_code == 200










    # # 获取所有菜单
    #
    # def test_getmenu(self):
    #     url = f"{self.address}/api/cloud/Permisssion/getMenu"
    #     payload = {}
    #     headers = {'X-Token': f'{self.token}'}
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     print(response.json())
    #     assert response.status_code == 200
    #
    # # 获取当前用户菜单
    # def test_getrights(self):
    #     url = f"{self.address}/api/cloud/Permisssion/getRights"
    #     payload = {}
    #     headers = {'X-Token': f'{self.token}'}
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     print(response.json())
    #     assert response.status_code == 200
    #
    # # 新增角色
    # @pytest.mark.parametrize('role_name,role_area', [('上海的', '021002')])
    # def test_newrole(self, role_name, role_area):
    #     role_name = role_name.encode("utf-8").decode("unicode_escape")
    #     url = f"{self.address}/api/cloud/Permisssion/newRole"
    #     payload = f'role_name={role_name}&role_area={role_area}'
    #     headers = {
    #         'X-Token': f'{self.token}',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     response = requests.post(url, headers=headers, data=payload)
    #     print(response.json()['result']['data']['result'])
    #     assert response.status_code == 200
    #     assert response.json()['result']['data']['result'] == True
    #
    # # 获取角色列表
    # @pytest.mark.parametrize('role_name,per_page,current_page', [('', '', '')])
    # def test_getroles(self, role_name, per_page, current_page):
    #     url = f"{self.address}/api/cloud/Permisssion/getRoles"
    #     payload = f'role_name={role_name}&per_page={per_page}&current_page={current_page}'
    #     headers = {
    #         'X-Token': f'{self.token}',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     response = requests.post(url, headers=headers, data=payload)
    #     print(response.json()['result']['data'])
    #     assert response.status_code == 200
    #     assert response.json()['result']['data'] != None
    #
    # # 删除角色信息
    # @pytest.mark.parametrize('role_id', [('')])
    # def test_deleterole(self, role_id):
    #     url = f"{self.address}/api/cloud/Permisssion/deleteRole"
    #     payload = f'role_id={role_id}'
    #     headers = {
    #         'X-Token': f'{self.token}',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     response = requests.post(url, headers=headers, data=payload)
    #     print(response.json()['result']['data']['result'])
    #     assert response.status_code == 200
    #     assert response.json()['result']['data']['result'] == True
    #
    # # 获取指定角色的权限菜单
    # @pytest.mark.parametrize('role_id', [('')])
    # def test_getRoleRights(self, role_id):
    #     url = f"{self.address}/api/cloud/Permisssion/getRoleRights"
    #     payload = f'role_id={role_id}'
    #     headers = {
    #         'X-Token': f'{self.token}',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     response = requests.post(url, headers=headers, data=payload)
    #     print(response.json()['result']['data'])
    #     assert response.status_code == 200
    #     assert response.json()['result']['data'] != None
    #
    # # 获取指定角色的服务地点
    # @pytest.mark.parametrize('role_id', [('')])
    # def test_getRoleRights(self, role_id):
    #     url = f"{self.address}/api/cloud/Permisssion/getRoleArea"
    #     payload = f'role_id={role_id}'
    #     headers = {
    #         'X-Token': f'{self.token}',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     response = requests.post(url, headers=headers, data=payload)
    #     print(response.json()['result']['data'])
    #     assert response.status_code == 200
    #     assert response.json()['result']['data'] != None
    #
    # # 新增用户
    # @pytest.mark.parametrize('user_name,password,role_id', [('sunyanan2', '123456', '1')])
    # def test_getroles(self, user_name, password, role_id):
    #     url = f"{self.address}/api/cloud/Permisssion/newUser"
    #     payload = f'user_name={user_name}&password={password}&role_id={role_id}'
    #     headers = {
    #         'X-Token': f'{self.token}',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     response = requests.post(url, headers=headers, data=payload)
    #     print(response.json())
    #     assert response.status_code == 200
    #     assert response.json()['result']['data']['result'] == True
    #
    # # 服务地点新增用户
    # @pytest.mark.parametrize('user_name,password,area_id', [('sunyanan4', '123456', '021002')])
    # def test_getroles(self, user_name, password, area_id):
    #     url = f"{self.address}/api/cloud/Permisssion/newUserByAreaId"
    #     payload = f'user_name={user_name}&password={password}&area_id={area_id}'
    #     headers = {
    #         'X-Token': f'{self.token}',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     response = requests.post(url, headers=headers, data=payload)
    #     print(response.json())
    #     assert response.status_code == 200
    #     assert response.json()['result']['data']['result'] == True
    #
    # # 获取用户列表,参数为空
    # @pytest.mark.parametrize('user_name,role_name,per_page,current_page', [('', '', '', '')])
    # def test_getroles(self, user_name, role_name, per_page, current_page):
    #     url = f"{self.address}/api/cloud/Permisssion/getUsers"
    #     payload = f'user_name={user_name}&role_name={role_name}&per_page={per_page}&current_page={current_page}'
    #     headers = {
    #         'X-Token': f'{self.token}',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     response = requests.post(url, headers=headers, data=payload)
    #     print(response.json()['result']['data'])
    #     assert response.status_code == 200
    #     assert response.json()['result']['data'] != None
    #
    # # 获取试点下的用户
    # @pytest.mark.parametrize('area_id', [('021002')])
    # def test_getroles(self, area_id):
    #     url = f"{self.address}/api/cloud/Permisssion/newUserByAreaId"
    #     payload = f'area_id={area_id}'
    #     headers = {
    #         'X-Token': f'{self.token}',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     response = requests.post(url, headers=headers, data=payload)
    #     print(response.json())
    #     assert response.status_code == 200
    #     assert response.json()['result']['data'] != None
    #
    # # 修改用户密码
    #
    # @pytest.mark.parametrize('user_id,password', [('021002', '123456')])
    # def test_updatePassword(self, user_id, password):
    #     url = f"{self.address}api/cloud/Permisssion/updatePassword"
    #     payload = f'user_id={user_id}&password={password}'
    #     headers = {
    #         'X-Token': f'{self.token}',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     response = requests.post(url, headers=headers, data=payload)
    #     print(response.json())
    #     assert response.status_code == 200
    #     assert response.json()['result']['data']['result'] == True
