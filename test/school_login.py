import time
import win32con
import ctypes
import random
import requests


def ErrorMessage(func):
    def wrapper(*args, **kw):
        print('函数名：{}  '.format(func.__name__))
        try:
            res = func(*args, **kw)
            print('执行成功！')
            return res
        except:
            print("执行失败！")
            return False
    return wrapper


@ErrorMessage
def get_info():
    host = 'https://gitee.com/haostart'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    print("is testing online")
    content = requests.get(host, headers, verify=False, timeout=1).text[50:100]
    print('content:', content)
    if '(haostart)' in content:
        return True
    return False


get_info()
with open('data.ini', 'r', encoding='utf=8') as f:
    a = f.readlines()

username = a[0].strip()
password = a[1].strip()
usermac = a[2].strip()

# test_1 = win32api.MessageBox(
#     0, f"用户名为：{username}\t\n密码为：{password}\t\nMAC地址为：{usermac}\t\n", "提醒", win32con.MB_OK)
ret = ctypes.windll.user32.MessageBoxTimeoutW(
    0, f"用户名为：{username}\t\n密码为：{password}\t\nMAC地址为：{usermac}\t\n", "提醒", win32con.MB_OK, 0, 2000)


def connect():
    ac_id = random.choice([1, 5, 61, 64])  # 一般无响应要更改ac_id
    print('当前ac_id：', ac_id)
    s = requests.session()

    res1 = s.post(
        url=r"http://172.30.16.34/srun_portal_pc.php",
        headers={
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN",
            "Cache-Control": "no-cache",
            "Connection": "Keep-Alive",
            "Content-Length": "109",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie": r"",
            # "Host": "172.30.16.34",
            'Origin': 'http://172.30.16.34',
            'X-Requested-With': 'XMLHttpRequest',
            "Referer": "",
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0)",
        },
        data={
            "ac_id": ac_id,
            "action": "login",
            "ajax": "1",
            "nas_ip": '',

            "username": username,
            "password": password,
            "save_me": "1",
            "user_ip": '',


            "user_mac": usermac,

        },
    



    )
    content = res1.content.decode()
    print(content + '\n')
    if (('login_ok' in content) or ('successful' in content)):

        print('\n登陆成功')

# def disconnect():
#     # hit_me()
#     username = '301737'
#     password = 'q13307023186'

#     # added_thread.start()
#     # print(username, password1)

#     s = requests.session()
#     # node = (node=uuid.getnode())
#     # mac = str(uuid.UUID(int=node).hex[-12:])
#     res1 = s.post(
#         url=r"http://172.30.16.34/include/auth_action.php",
#         headers={
#             "Accept": "*/*",
#             "Accept-Encoding": "gzip, deflate",
#             "Accept-Language": "zh-CN",
#             "Cache-Control": "no-cache",
#             "Connection": "Keep-Alive",
#             "Content-Length": "109",
#             "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
#             "Cookie": r"login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrvEe0UJsHZAaiCmY%252FDhrV2LGMuD3%252BcoyqSZ2EWX584sBybRJ9yo2fv1XBj03H9tPWkZeCauuZKGqBXEvY5Uj7c%252B7RAja6qTtMcfLVPUO0d8RWEGoBJKZbRGHhaebZ4tqDu0UigxN%252FdxIoN%252FKZj%252FR1NawQelQ9VXNV7PvoTltlG2siUnL29VAxXTXLPSz97LcDkxhlXsEACziYiTQ%253D%253D; login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrvEe0UJsHZAaiCmY%252FDhrV2LGMuD3%252BcoyqSZ2EWX584sBybRJ9yo2fv1XBj03H9tPWkZeCauuZKGqBXEvY5Uj7c%252B7RAja6qTtMcfLVPUO0d8RWEGoBJKZbRGHhaebZ4tqDu0UigxN%252FdxIoN%252FKZj%252FR1NawQelQ9VXNV7PvoTltlG2siUnL29VAxXTXLPSz97LcDkxhlXsEACziYiTQ%253D%253D; NSC_tsvo_4l_TH=ffffffffaf160e3b45525d5f4f58455e445a4a423660",
#             "Host": "172.30.16.34",
#             'Origin': 'http://172.30.16.34',
#             'X-Requested-With': 'XMLHttpRequest',
#             "Referer": "http://172.30.16.34/srun_portal_pc.php?ac_id=1&cmd=login&switchip=172.30.14.104&mac=90:78:41:ea:2e:be&ip=10.112.237.190&essid=WHUT-WLAN-DORM&apname=XS-JH-018-611-AP303&apgroup=WHUT-DORM-Dual-HD&url=http://www.gstatic.com/generate_204",
#             "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0)",
#         },
#         data={

#             "action": "logout",
#             "ajax": "1",


#             "username": username,
#             "password": password,


#         },


#     )
#     content = res1.content
#     content = content.decode()
#     print(content + '\n')
#     if (('login_ok' in content) or ('successful' in content)):

#         print('\n登陆成功')


def con_1():
    try:

        if get_info():
            ret = ctypes.windll.user32.MessageBoxTimeoutW(
                0, '已经联网了！', "提醒", win32con.MB_OK, 0, 2000)

            print('已经联网了！')
            time.sleep(1)
            return
    except:
        pass
        # win32api.MessageBox(
        #     0, '准备联网中，需要过几秒，请10s后刷新网页试试！', "提醒", win32con.MB_OK)
    t = 10
    flag = 1
    while(t):
        t -= 1
        try:

            connect()
            print('连接ing.........')
            time.sleep(1)
            if get_info():
                ret = ctypes.windll.user32.MessageBoxTimeoutW(
                    0, '已经联网了！', "提醒", win32con.MB_OK, 0, 2000)

                print('已经联网了！')
                flag = 0
                break
            else:
                print('失败！')
        except:
            print('失败！')
    if flag == 1:
        if get_info():
            ret = ctypes.windll.user32.MessageBoxTimeoutW(
                0, '已经联网了！', "提醒", win32con.MB_OK, 0, 2000)

            print('已经联网了！')

        else:
            ret = ctypes.windll.user32.MessageBoxTimeoutW(
                0, '10次尝试均联网失败，查看是否连接上WHUT-WLAN-DORM', "提醒", win32con.MB_OK, 0, 4000)


con_1()

# if __name__ == "__main__":
#     # read_file()
#     if input() == str(1):
#         disconnect()
#     else:

#         con_1()
