"""
    @Author Harveywei
    @Date 2022/9/20 20:36
    @Describe
    @Version 1.0
"""

from whutpy import cwsf
usernname=''
password=''

if __name__ == '__main__':
    client=cwsf.CwsfClient(username=usernname,password=password)
    client.login()
    print(client.remainingElectricityBill(meterId='0311.000397.1'))  #查看寝室剩余电费 例子：此id为东院东1一楼101
    print(client.lastPayTime())  #查看最后一次缴纳网费的时间