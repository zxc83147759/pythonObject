from selenium import webdriver
import time


# function
class auto_Table:
    def __init__(self):
        pass

    def xpath_one(self, input_tr, which_one):
        driver.find_element_by_xpath(
            '/html/body/form/table/tbody/tr[%d]/td[2]/input[%d]' % (input_tr, which_one)).click()

    def xpath(self, x, y):
        for i in range(x, y):
            try:
                driver.find_element_by_xpath(
                    '/html/body/form/table/tbody/tr[%d]/td[2]/input[2]' % (i)).click()
            except:
                continue
            return 0

    def Id(self, str1, x, y, z):
        for i in range(x, y, z):
            driver.find_element_by_id('%s%03d' % (str1, i)).click()
            return 0

    def close_webpage(self):
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        driver.close()
        driver.switch_to.window(handles[0])
        return 0


driver = webdriver.Chrome()
url = 'https://info.stu.edu.tw/ePortal/login.asp'  # 網址
driver.get(url)
title = driver.title  # title方法可以獲取當前頁面的標題顯示的欄位
while title == 'Campus Information Services':
    account = input('輸入帳號:')
    password = input('輸入密碼:')
    driver.find_element_by_id('account').send_keys(account)  # 帳號輸入
    driver.find_element_by_id('password').send_keys(password)  # 密碼輸入
    Captcha = input('輸入驗證碼:')
    driver.find_element_by_id('captcha').send_keys(Captcha)  # 驗證碼輸入
    driver.find_element_by_id('btnSubmit').click()  # 登入按鈕
    title = driver.title
    if title != 'Portal Index':
        break
    else:
        print('帳號密碼或驗證碼輸入錯誤')
        driver.find_element_by_xpath(
            '/html/body/div/div[1]/div/div[2]/div/div[3]/div[5]/div/div[2]/a').click()
        continue

url = 'https://info.stu.edu.tw/aca/student/CoStuAns/StuOpinion.asp'
driver.get(url)
title = driver.title
table_count = 0
AT = auto_Table()
while title == '教學評量系統':
    try:
        driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[%d]' % (table_count)).click()
        title = driver.title
        table_count += 1
    except:
        table_count += 1
        continue
    if title == '問卷填寫畫面':
        if driver.find_element_by_xpath('/html/body/form/center/font[2]').text == '教學成效問卷_F卷 體育課程':
            AT.xpath(2, 30)
            AT.xpath_one(13, 5)
            AT.xpath_one(14, 2)
            AT.xpath_one(24, 6)
            AT.xpath_one(25, 1)
            AT.xpath_one(26, 2)
            AT.xpath_one(27, 1)
        elif driver.find_element_by_xpath('/html/body/form/center/font[2]').text == '教學成效問卷_E卷 專題課程':
            AT.Id('A189', 3, 45, 5)
        elif driver.find_element_by_xpath('/html/body/form/center/font[2]').text == '教學成效問卷_D卷 實習課程':
            AT.Id('A190', 3, 40, 5)
        elif driver.find_element_by_xpath('/html/body/form/center/font[2]').text == '教學成效問卷_A卷 一般課程':
            AT.xpath_one(2, 6)
            AT.xpath_one(3, 1)
            AT.xpath_one(4, 2)
            AT.xpath_one(5, 1)
            AT.xpath(6, 8)
            driver.find_element_by_id('A193037').click()
            driver.find_element_by_id('A193047').click()
            driver.find_element_by_id('A193052').click()
            driver.find_element_by_id('A193060').click()
            AT.Id('A193', 63, 135, 5)
        driver.find_element_by_id('upset1').click()

    if title == '樹德科技大學導師制度之學生評量表':
        AT.close_webpage()
        for j in range(17, 20):
            driver.find_element_by_xpath(
                '/html/body/center/form[1]/table[2]/tbody/tr[%d]/td[2]/p/font/input[3]' % (j)).click()
        for j in range(20, 27):
            driver.find_element_by_xpath(
                '/html/body/center/form[1]/table[2]/tbody/tr[%d]/td[2]/p/input[2]' % (j)).click()
        driver.find_element_by_id('InsDa').click()
        AT.close_webpage()
        # driver.find_element_by_xpath('//*[@id="form"]/table/tbody/tr/th/table/tbody/tr[2]/td/p/a').click()

    if title == '':
        driver.find_element_by_xpath(
            '//*[@id="form1"]/div/table/tbody[2]/tr/td[4]/input[1]').click()
        title = driver.title
        if title == '105年第1學期教學成效問卷_學生':
            for i in range(1, 19):
                driver.find_element_by_xpath(
                    '//*[@id="questions"]/ol/li[%d]/ul/li[2]/input' % (i)).click()
            driver.find_element_by_id('sendData').click()
    table_count = 0
    url = 'https://info.stu.edu.tw/aca/student/CoStuAns/StuOpinion.asp'
    driver.get(url)
    title = driver.title
    if driver.find_element_by_xpath('/html/body/center/font').text == '已無需施做之評量':
        print('填寫完畢，感謝使用')
        break
    else:
        continue

print('關閉中....')
time.sleep(3)
driver.quit()
