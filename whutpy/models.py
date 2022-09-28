"""
    @Author Harveywei
    @Date 2022/9/20 20:36
    @Describe
    @Version 1.0
"""
class WhutUrl:
    CWSF_URL='http://cwsf.whut.edu.cn/'
    WHUT_NET_AUTH='http://172.30.16.34/'
    ZHLGD_URL='http://zhlgd.whut.edu.cn/'



class Endpoints:
    #CWSF
    CWSF_LOGIN=WhutUrl.CWSF_URL+'innerUserLogin'
    QUERY_RESERVE=WhutUrl.CWSF_URL+'queryReserve'
    PAY_LIST=WhutUrl.CWSF_URL+'queryPayOrderList'

    #WHUT_NET
    NET_AUTH=WhutUrl.WHUT_NET_AUTH+'include/auth_action.php'

    #ZHLGD
    ZHLGD_LOGIN=WhutUrl.ZHLGD_URL+'tpass/login'
    CARD_CONSUM_API=WhutUrl.ZHLGD_URL+'tp_up/up/sysintegration/getCardConsumList'
    TP_UP=WhutUrl.ZHLGD_URL+'tp_up/'
    GET_CARD_MONEY=WhutUrl.ZHLGD_URL+'tp_up/up/sysintegration/getCardMoney'
    UNREADE_MESSAGE=WhutUrl.ZHLGD_URL+'tp_up/sys/uacm/msgcenter/getSelUnReadCount'


class Headers:
    CWSF_HEADERS={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate',

    }

    AUTH_ACTION_HEADERS={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': '172.30.16.34',
        'Origin': 'http://172.30.16.34',
        'Referer': 'http://172.30.16.34/srun_portal_pc.php?ac_id=5&url=jwc.whut.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    ZHLGD_HEADERS={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'zhlgd.whut.edu.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    GET_CARD_MONEY_HEADERS={
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection':'keep-alive',
        'Content-Length':'2',
        'Content-Type':'application/json;charset=UTF-8',
        'Host':'zhlgd.whut.edu.cn',
        'Origin':'http://zhlgd.whut.edu.cn',
        'Referer':'http://zhlgd.whut.edu.cn/tp_up/view?m=up',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
    }

    GET_CARD_CONSUMLIST_HEADERS={
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection':'keep-alive',
        'Content-Length':'130',
        'Content-Type':'application/json;charset=UTF-8',
        'Cookie':'Language=zh_CN; JSESSIONID=fABlNz-zNzsrvAD0a9OiG1MyN_NRU7B-ntV_i2HOiFFctL66ZVOV!-1701493779; tp_up=h7plOsOBbWWK5BDcVjXFtC95FN79N8GioHZcCXxYbl4ojYxuJJGF!59120401',
        'Host':'zhlgd.whut.edu.cn',
        'Origin':'http://zhlgd.whut.edu.cn',
        'Referer':'http://zhlgd.whut.edu.cn/tp_up/view?m=up',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
    }
    UNREAD_MESSAGE_HEADERS={
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection':'keep-alive',
            'Content-Length':'2',
            'Content-Type':'application/json;charset=UTF-8',
            'Host':'zhlgd.whut.edu.cn',
            'Origin':'http://zhlgd.whut.edu.cn',
            'Referer':'http://zhlgd.whut.edu.cn/tp_up/view?m=up',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
        }
