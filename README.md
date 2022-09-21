Whut Information Query for Python
=======

`whutpy` 是一个基于python的库

`whutpy` 能够使用用户密码登录whut的各种网站查询生活中需要的信息和减少重复的日常工作（无需传递sessionId和webcookie）

`whutpy` 是使用 Python 3 开发的，使用类型提示和许多其他功能，支持 Windows、Linux 和 MacO。


Table of Content
================
* [Examples](https://github.com/Harveyweiii/whutpy#examples)

* [Cwsf methods](https://github.com/Harveyweiii/whutpy#steamclient-methods)

* [Whutnet methods](https://github.com/Harveyweiii/whutpy#market-methods)


Usage
=======

Examples
========



Cwsf Methods
===================
**CSWF查看宿舍电费,查看最后一次网费提交时间**

```python
from whutpy.cwsf import CwsfClient    

cwsfclient = CwsfClient(username='',password='')
print(cwsfclient.remainingElectricityBill(meterId='0311.000397.1'))  #查看寝室剩余电费 例子：此id为东院东1一楼101
print(cwsfclient.lastPayTime())  #查看最后一次缴纳网费的时间
```


Whutnet Methods
===================
```python
from whutpy.whutNet import WhutNetClent    

net=WhutNetClent(username='',password='')
net.login() #登录
net.logout() #登出
```



License
=======

MIT License

Copyright (c) 2022 [Harveyweiii](harvey_wei@foxmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.