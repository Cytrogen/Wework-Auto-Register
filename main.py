import datetime
from users import get_number, get_user_choice, get_user_choice_single_day, get_user_choice_multi_days
from drivers import reserve_single_day, reserve_multi_days

if __name__ == '__main__':
    today = datetime.date.today()
    print('欢迎使用WeWork自动预约系统！')
    print(f'当前日期为 {today} 。（预约时会使用这个日期，如快要临近第二日，请在凌晨0点后重新运行该程序）')

    while True:
        choice = get_user_choice()
        match choice:
            case 1:  # 预约单日
                reserve_choice = get_user_choice_single_day()
                match reserve_choice:
                    case 1:  # 预约明天
                        reserve_single_day(today.day + 1)
                    case 2:  # 自定义日期
                        custom_date = get_number('输入自定义日期：')
                        reserve_single_day(custom_date)
                    case _:
                        print('无效的号码！')

            case 2:  # 批量预约
                dates_list = get_user_choice_multi_days('输入日期（使用&分割）：')
                reserve_multi_days(dates_list)

            case _:
                print('不在选择范畴内的号码！')
