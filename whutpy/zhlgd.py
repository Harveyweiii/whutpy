"""
    @Author Harveywei
    @Date 2022/9/20 20:40
    @Describe 
    @Version 1.0
"""
import logging
import re
import time
import pandas as pd
import requests
from whutpy.models import Headers,Endpoints
import execjs

class ZhlgdClient:
    def __init__(self,username:str=None,password:str=None):
        self.username=username
        self._password=password
        self._session=requests.session()
        self._session.headers=Headers.ZHLGD_HEADERS

    def login(self)->None:

        response=self._session.post(url=Endpoints.ZHLGD_LOGIN,data=self.__login_data(),headers=Headers.ZHLGD_HEADERS)
        if '用户名密码错误' in response.text:
            raise ValueError('用户名密码错误,登录失败')
        else:
            logging.info('登录成功')
        time.sleep(0.2)
        response=self._session.get(url='http://zhlgd.whut.edu.cn/tp_up/')
        response=self._session.get(url='http://zhlgd.whut.edu.cn/tpass/login?service=http%3A%2F%2Fzhlgd.whut.edu.cn%2Ftp_up%2F')


    def getCardConsumInfo(self,startDate:str='',endDate:str='',outputTimes:int=10)->[]:
        """

        :param startDate:账单开始的时间 默认不填为最近
        :param endDate:账单结束的时间 默认不填为最近
        :param outputTimes:输出这段时间多少条消费记录 若为-1则全输出
        :return:
        """
        TOTAL_CONSUM_TIMES=int(self.__postCardConsumUrl(startDate=startDate,endDate=endDate)['total'])
        if outputTimes>TOTAL_CONSUM_TIMES or outputTimes==-1:
            outputTimes=TOTAL_CONSUM_TIMES

        pages=outputTimes/10
        res=[]
        for page in range(1,int(pages)+1):
            jdata=self.__postCardConsumUrl(startDate,endDate,pageNum=page)
            for item in jdata['list']:
                time_str=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['JYSJ']/1000))
                res.append([item['ROW_ID'],time_str,item['JYJE']/100,item['SH_NAME'].replace(' ','')])
            time.sleep(0.2)
        return res

    def cardCosumeToExcel(self,startDate:str='',endDate:str='',outputTimes:int=10,outputfile:str='./消费记录.xlsx'):
        df=pd.DataFrame(self.getCardConsumInfo(startDate=startDate,endDate=endDate,outputTimes=outputTimes),columns=['序号','时间','消费','地点'])

        df.to_excel(outputfile)
        pass

    def __postCardConsumUrl(self,startDate:str='',endDate:str='',pageNum:int=1):
        self._session.headers['Content-Type'] = 'application/json;charset=UTF-8'
        return self._session.post(Endpoints.CARD_CONSUM_API,json=self.__cardconsum_postdata(startDate=startDate,endDate=endDate,pageNum=pageNum)).json()


    def getCardMoney(self)->float:
        response=self._session.post(url=Endpoints.GET_CARD_MONEY,headers=Headers.GET_CARD_MONEY_HEADERS,json={})
        return float(response.json()['KHYE'])/100


    def checkUnreadMessage(self) ->int:
        psdt={}
        response=self._session.post(url=Endpoints.UNREADE_MESSAGE,headers=Headers.UNREAD_MESSAGE_HEADERS,json=psdt).json()
        return int(response['UN_MSG_COUNT'])



    def __login_data(self)->dict:
        url = Endpoints.ZHLGD_LOGIN
        ul=len(self.username)
        pl=len(self._password)
        response=self._session.get(url=url).text
        lt=re.findall('value=\"(LT.*?)\"',response)[0]
        execution = re.findall('name="execution" value="(.*?)"', response)[0]

        with open('../whutpy/des.js')as f:
            ctx = execjs.compile(f.read())
        rsa=ctx.call('strEnc',self.username+self._password+lt,'1','2','3')

        return {
            'rsa': rsa,
            'ul':ul,
            'pl':pl,
            'lt':lt,
            'execution': execution,
            '_eventId': 'submit'
        }

    def __cardconsum_postdata(self,startDate:str='',endDate:str='',pageNum:int=1) ->dict:
        return {
            'appointTime': "",
            'dateSearch':"",
            'draw':'1',
            'endDate':endDate,
            'length':'10',
            'order':[],
            'pageNum':pageNum,
            'pageSize': '10',
            'start':'0',
            'startDate':startDate
}