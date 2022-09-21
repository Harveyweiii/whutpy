"""
    @Author Harveywei
    @Date 2022/9/20 20:36
    @Describe
    @Version 1.0
"""

import requests
from whutpy.models import Endpoints,Headers
import base64
class WhutNetClent():
    def __init__(self,username:str=None,password:str=None) ->None:
        self.username=username
        self._password=password

    def login(self) ->bool:
        url=Endpoints.NET_AUTH
        post_data={
            'action': 'login',
            'username': self.username,
            'password': '{B}'+base64.b64encode(self._password.encode('utf-8')).decode("utf-8"),
            'ac_id': '5',
            'user_ip':'',
            'nas_ip':'',
            'user_mac':'',
            'save_me': '1',
            'ajax': '1',
        }
        response=requests.post(url,data=post_data,headers=Headers.AUTH_ACTION_HEADERS)
        if 'login_ok' in response.text:
            print(response.text)
            return True
        else:
            return False


    def logout(self) ->bool:
        url=Endpoints.NET_AUTH
        post_data={
            'action': 'logout',
            'username': self.username,
            'password': self._password
        }
        try:
            response=requests.post(url=url,data=post_data,headers=Headers.AUTH_ACTION_HEADERS)
            return True
        except:
            return False
