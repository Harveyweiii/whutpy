"""
    @Author Harveywei
    @Date 2022/9/20 22:17
    @Describe 
    @Version 1.0
"""
username=''
password=''


from whutpy import zhlgd

if __name__ == '__main__':
    client=zhlgd.ZhlgdClient(username=username,password=password)
    client.login()

    # print(client.checkUnreadMessage())
    # print(client.getCardConsumInfo(outputTimes=50)) #输出最近50次消费记录
    # print(client.getCardConsumInfo(outputTimes=-1)) #输出所有消费记录
    # print(client.getCardConsumInfo(outputTimes=50,startDate='2022-01-20',endDate='2022-09-01'))  # 输出最近50次消费记录
    client.cardCosumeToExcel(outputfile='./消费记录.xlsx',startDate='',endDate='',outputTimes=10) #输出到excel


    # print(client.getCardMoney()) #查看校园卡余额