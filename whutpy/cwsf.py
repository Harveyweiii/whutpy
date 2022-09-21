"""
    @Author Harveywei
    @Date 2022/9/20 20:36
    @Describe
    @Version 1.0
"""
import time

import requests
import tesserocr
from lxml import etree

from whutpy.models import Endpoints,Headers,WhutUrl
from PIL import Image, ImageFilter


class CwsfClient():
    def __init__(self,username : str =None, password : str = None) -> None:
        self.username=username
        self._password=password
        self._session=requests.session()
        self._session.headers=Headers.CWSF_HEADERS
        self.was_login_executed=False



    def login(self) ->None:
        url =Endpoints.CWSF_LOGIN

        pag_text=self._session.post(url,verify=False).text
        tree = etree.HTML(pag_text)
        img_path = WhutUrl.CWSF_URL + tree.xpath('//*[@id="platform-body"]/tr[4]/td[3]/img/@src')[0]
        img_content = self._session.get(img_path, verify=False).content
        with open('temp.png','wb') as f:
            f.write(img_content)
        img_code=self._codeRecognition('temp.png')

        data = {
            'nickName': self.username,
            'logintype': 'PLATFORM',
            'password': self._password,
            'checkCode': img_code
        }
        # print(data)
        time.sleep(1)
        response=self._session.post(url=url,data=data,verify=False)

        if  '用户不存在' in response.text:
            raise ValueError('用户不存在')
        elif '密码错误' in response.text:
            raise ValueError('密码错误')
        elif '验证码输入错误' in response.text:
            raise ValueError('验证码输入错误')
        else:
            self.was_login_executed=True
            log='[登录状况]登录成功'


    def _codeRecognition(self,code_path:str) ->str:
        image=Image.open(code_path)
        image = image.convert('L')
        threshold = 127
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        image = image.point(table, '1')
        # image2.show()  # 二值化灰度处理图片显示
        image = image.crop((1, 1, 69, 19))
        image = image.filter(ImageFilter.SHARPEN)
        code=tesserocr.image_to_text(image)
        code=code.replace(" ", "").replace("\n", "")
        return code


    def remainingElectricityBill(self,meterId:str)->str:
        #查看电费
        url=Endpoints.QUERY_RESERVE
        post_data={
            'meterId': meterId,
            'factorycode': 'E035'
        }
        response=self._session.post(url,data=post_data)

        log='[电费查询]\n电费剩余{}元\n电量剩余{}度'.format(response.json()['meterOverdue'],response.json()['remainPower'])
        return log

    def lastPayTime(self)->str:
        url=Endpoints.PAY_LIST
        log='[上一次网络缴费时间]:\n'
        post_data={
            "idesrial":"",
            "orderno": "",
            "payflag": "2",
            "createbegintime": "",
            "createendtime": "",
            "payproid": "",
            "page": "1",
            "pagesize": 6
        }
        headers=Headers.CWSF_HEADERS
        headers['Content-Type']='application/json;charset=UTF-8'
        response=self._session.post(url,json=post_data,headers=headers,verify=False)
        for payOrder in response.json()['payOrderList']:
            if payOrder['payproname']=='网络使用费':
                return log+payOrder['paytime']

