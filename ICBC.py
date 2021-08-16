'''
    中国工商银行账户管理系统：
        ICBC:
'''
import random

# 1.准备一个数据库 和 银行名称
bank = {}  # 空的数据库

'''
    {
        "张三":{
            account:s001,
            country:"中国"
        }，
        "李四":{

        }

0
    }

'''
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


# 2.入口程序
def welcome():
    print("*************************************")
    print("*      中国工商银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                          =     *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    # 1.判断数据库是否已满
    if len(bank) >= 100:
        return 3
    # 2.判断用户是否存在
    if username in bank:
        return 2
    # 3.正常开户
    bank[account] = {
        "username": username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "gate": gate,
        "money": money,
        "bank_name": bank_name
    }
    return 1


# 用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))  # 将输入金额转换成int类型
    # 随机产生8为数字
    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password, country, province, street, gate, money)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                 省份：%s
                 街道：%s
                 门牌号: %s
             余额：%s
             开户行地址：%s
             ------------------------
         '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name))


def bank_savemoney(account, smoney):
    # 1.判断用户是否存在用户库中
    if account in bank:
        # 正常存款
        bank[account]["money"] = bank[account]["money"] + smoney

        return 4
    else:
        return 5


# def check_bank(account):
#     for key in bank:
#         bank[key] == account


def savemoney():
    account = int(input("请输入你的存款账号："))
    smoney = int(input("请输入你存款金额："))
    status = bank_savemoney(account, smoney)
    if status == 4:
        print("++++++")
        print("存款成功，您的账户余额是：{}".format(bank[account]["money"]))
    if status == 5:
        print("False")


def bank_take(account, password, tmoney):
    # 判断是否存在该账户
    if account not in bank:
        return 1
    elif account in bank:
        # 密码是否正确

        if bank[account]["password"] != password:
            return 2
        elif bank[account]["password"] == password:
            if bank[account]["money"] < tmoney:
                return 3
            elif bank[account]["money"] >= tmoney:
                bank[account]["money"] = bank[account]["money"] - tmoney
                return 4


def takemoney():
    account = int(input("请输入你的账号："))
    password = input("请输入你的密码：")
    tmoney = int(input("请输入你要取的金额："))
    status = bank_take(account, password, tmoney)
    if status == 1:
        print("该账户不存在")
    if status == 2:
        print("密码输入错误")
    if status == 3:
        if tmoney > bank[account]["money"]:
            print("您的账户余额不足")
    if status == 4:
        #     bank[account["money"]]=bank[account]["money"]-tmoney
        print("你的账户还有：{}".format(bank[account]["money"]))


def bank_transfer(account1, account2, password1, tranmoney):
    if account1 not in bank or account2 not in bank:
        return 1
    elif account1 in bank and account2 in bank:
        if bank[account1]["password"] != password1:
            return 2
        elif bank[account1]["password"] == password1:
            if bank[account1]["money"] < tranmoney:
                return 3
            elif bank[account1]["money"] >= tranmoney:
                bank[account1]["money"] = bank[account1]["money"] - tranmoney
                bank[account2]["money"] = bank[account2]["money"] + tranmoney
                return 4


def tranfer():
    account1 = int(input("请输入转出账户："))
    account2 = int(input("请输入转入账户："))
    password1 = input("请输入转出账户密码：")
    tranmoney = int(input("请输入转账金额："))
    status = bank_transfer(account1, account2, password1, tranmoney)
    if status == 1:
        print("账户不存在")
    elif status == 2:
        print("密码错误")
    elif status == 3:
        print("您的账户余额不足")
    elif status == 4:
        print("转账成功，您的账户余额：{}，转入账户余额：{}".format(bank[account1]["money"], bank[account2]["money"]))


def bank_information(account, password):
    if account not in bank:
        return 1
    elif account in bank:
        if bank[account]["password"] != password:
            return 2
        elif bank[account]["password"] == password:
            return 3


def information():
    account = int(input("请输入账户"))
    password = input("请输入密码")
    status = bank_information(account, password)
    if status == 1:
        print("账户错误")
    elif status == 2:
        print("密码错误")
    elif status == 3:
        print("以下是您的个人信息：")
        info = '''
            ----------个人信息------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                 省份：%s
                 街道：%s
                 门牌号: %s
             余额：%s
             开户行地址：%s
             ------------------------
         '''
        print(info % (bank[account]["username"], password, account, bank[account]["country"], bank[account]["province"],
                      bank[account]["street"],
                      bank[account]["gate"], bank[account]["money"], bank_name))


while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        savemoney()
    elif chose == "3":
        takemoney()
    elif chose == "4":
        tranfer()
    elif chose == "5":
        information()
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")