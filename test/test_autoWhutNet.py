"""
    @Author Harveywei
    @Date 2022/9/20 20:36
    @Describe
    @Version 1.0
"""

from whutpy import whutNet
username=''
password=''



if __name__ == '__main__':
    net=whutNet.WhutNetClent(username=username,password=password)
    net.login() #登录
    # net.logout() #登出
