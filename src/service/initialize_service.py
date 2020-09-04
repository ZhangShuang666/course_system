from src.models import Admin


def initialize():
    try:
        username = input("请输入用户名称：")
        password = input("请输入密码：")
        obj = Admin(username, password)
        obj.save()
        return True
    except Exception as e:
        print(e)


def main():
    show = """
            '1': 初始化管理账号
    """
    choice_dict = {
        '1': initialize
    }
    while True:
        print(show)
        choice = input("请输入操作选项：")
        if choice not in choice_dict:
            print("选项错误，请重新输入！！！")
            continue
        func = choice_dict[choice]
        ret = func()
        if ret:
            print('操作成功')
        else:
            print('操作异常，请重试')


if __name__ == "__main__":
    main()


