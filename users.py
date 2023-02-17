def get_number(text):
    """
    获取用户输入的数字。
    :param text: 问题文本
    :return number: 数字
    """
    while True:
        try:
            number = int(input(text).strip())
            return number
        except ValueError:
            print('无效的输入！')


def get_user_choice():
    """
    获取用户主菜单选项号码：
    1. 预约单日；
    2. 批量预约。
    :return user_choice: 用户选项号码
    """
    print('1. 预约单日')
    print('2. 批量预约')
    user_choice = get_number('输入号码：')
    return user_choice


def get_user_choice_single_day():
    """
    获取用户预约单日菜单选项号码：
    1. 预约明天；
    2. 自定义预约日期。
    :return user_choice: 用户选项号码
    """
    print('1. 预约明天')
    print('2. 自定义预约日期')
    user_choice = get_number('输入号码：')
    return user_choice


def get_user_choice_multi_days(text):
    """
    获取用户输入的多串数字，并切割成列表。
    :param text: 问题文本
    :return numbers_list: 日期列表
    """
    while True:
        try:
            numbers_list = input(text).strip().split('&')
            numbers_list = list(map(int, numbers_list))
            return numbers_list
        except ValueError:
            print('无效的输入！')
