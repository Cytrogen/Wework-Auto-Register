from time import sleep
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from config import Config


def get_driver(is_headless=Config.is_headless):
    """
    获取浏览器对象。
    :param is_headless: 是否开启无头模式（不显示浏览器）
    :return driver: 浏览器对象
    """
    driver = None
    match is_headless:
        case True:
            options = Options()
            options.add_argument('--headless')
            driver = webdriver.Edge(options=options)
        case False:
            driver = webdriver.Edge()
    return driver


def driver_do(driver, condition, by='XPATH', action=None, key=None):
    """
    对浏览器对象进行操作。
    :param driver: 浏览器对象
    :param condition: 查找元素时的条件。如使用XPATH查询，填写XPATH；如使用ID查询，填写标签ID
    :param key: 对元素进行文本提交时的文本
    :param by: 使用XPATH还是ID查询元素
    :param action: 对元素进行点击操作还是文本提交操作
    :return None:
    """
    while True:
        try:
            match by:
                case 'XPATH':
                    behavior = driver.find_element(By.XPATH, condition)
                case 'ID':
                    behavior = driver.find_element(By.ID, condition)
                case _:
                    print('driver_do() 错误的使用方式')
                    exit(1)
            match action:
                case 'click':
                    behavior.click()
                case 'send_keys':
                    behavior.send_keys(key)
                case _:
                    pass
            break
        except (NoSuchElementException, ElementNotInteractableException):
            sleep(1)
    return None


def simulate_login(driver):
    """
    模拟登录。
    :param driver: 浏览器对象
    :return None:
    """
    print('登录中...')
    driver_do(driver, condition='1-email', by='ID', action='send_keys', key=Config.email)
    driver_do(driver, condition='1-password', by='ID', action='send_keys', key=Config.password)
    driver_do(driver, condition='1-submit', by='ID', action='click')
    print('进入预约页面中...')
    driver_do(driver, condition='//*[@id="root"]/div/div[2]/div/div[2]/ul/li[2]/div', by='XPATH', action='click')
    driver_do(driver, condition='/html/body/div[2]/div/div/a[2]', by='XPATH', action='click')
    return None


def reserve_single_day(date):
    """
    预约单日。
    :param date: 预约日期
    :return None:
    """
    print('开始预约...')
    driver = get_driver()
    print('打开网页...')
    driver.get('https://members.wework.com')
    simulate_login(driver)
    sleep(5)
    print('选择日期中...')
    driver_do(driver, condition='//*[@id="root"]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/input', by='XPATH', action='click')
    driver_do(driver, condition=f'//*[contains(@class, "DayPicker-Day--selected")]/../..//*[text()="{date}"]', by='XPATH', action='click')
    print('选择地点中...')
    driver_do(driver, condition=f'//div[text()="{Config.address}"]/../../../../section/button', by='XPATH', action='click')
    print('预约中...')
    try:
        sleep(2)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div[2]/span[3]/button[text()="Book for 0 credits"]').click()
    except NoSuchElementException:
        print('无法预约！可能是已经预约过了！如有错请手动预约！')
        exit(1)
    print('预约成功！')
    driver.quit()
    print()
    return None


def reserve_multi_days(dates_list):
    """
    预约多日。
    :param dates_list: 日期列表
    :return None:
    """
    print('开始预约...')
    driver = get_driver()
    print('打开网页...')
    driver.get('https://members.wework.com')
    simulate_login(driver)
    for date in dates_list:
        sleep(5)
        print(f'选择日期 {date} 中...')
        driver_do(driver, condition='//*[@id="root"]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/input', by='XPATH', action='click')
        sleep(1)
        driver_do(driver, condition=f'//*[contains(@class, "DayPicker-Day--selected")]/../..//*[text()="{date}"]', by='XPATH', action='click')
        print('选择地点中...')
        driver_do(driver, condition='//div[text()="214 W 29th St"]/../../../../section/button', by='XPATH', action='click')
        print('预约中...')
        try:
            sleep(2)
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/span[3]/button[text()="Book for 0 credits"]').click()
            print(f'日期 {date} 预约成功！')
        except NoSuchElementException:
            print(f'无法预约日期 {date} ！可能是已经预约过了！如有错请手动预约！')
            driver_do(driver, condition='/html/body/div[2]/div/div[2]/span[1]/button', by='XPATH', action='click')
            continue
        driver_do(driver, condition='/html/body/div[2]/div/div[2]/span[3]/button', by='XPATH', action='click')
        sleep(2)
    print('全部预约成功！')
    driver.quit()
    return None
