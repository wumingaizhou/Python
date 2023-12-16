# 银行取钱案例

# 1.界面
money = 1500
def main_ul():
    input_1 = int(input("""
    --------------主菜单--------------
    吴名，你好，欢迎来到中国银行，请输入操作：
    查询余额 [输入1]
    存钱    [输入2]
    取钱    [输入3]
    退出    [输入4]
    请输入你的选择: """))
    if input_1 == 1:
        CheckMoney()
    elif input_1 == 2:
        SaveMoney()
    elif input_1 == 3:
        GetMoney()
    elif input_1 == 4:
        print("""
    你已退出""")
    else:
        print("""
    输入错误，请重新输入""")
        main_ul()

# 2.查询钱函数
def CheckMoney():

    print(f"""
    --------------查询余额--------------
    吴名，你好，你的余额剩余：{money}元
    """)
    input("")
    main_ul()

# 2.取钱函数
def GetMoney():
    num2 = int(input("""
    --------------取钱--------------
    吴名，你好，请输入你要取的钱： """))
    global money
    money -= num2
    print(f"""
    吴名，你取钱{num2}元成功""")
    print(f"""
    吴名，你的余额剩余{money}元""")
    input("")
    main_ul()

# 2.存钱函数
def SaveMoney():
    num1 = int(input("""
    --------------存钱--------------
    吴名，你好，请输入你要存的钱： """))
    global money
    money += num1
    print(f"""
    吴名，你好，你存钱成功，余额为{money}""")
    input("")
    main_ul()

main_ul()
