from selenium import webdriver


driver = webdriver.Firefox()
url = 'https://info.stu.edu.tw/ePortal/login.asp'  # 網址
driver.get(url)
driver.maximize_window()
account = 's17113115'
password = ''
# 帳號輸入
driver.find_element_by_id('account').send_keys(account)
# 密碼輸入
driver.find_element_by_id('password').send_keys(password)

'''
沒有id時可使用xpath
F12->提交按鈕右鍵檢查->右鍵copy->copy XPath
click 點擊
send_keys 可輸入想要的值
driver.find_element_by_link_text("新聞").click()
print(driver.title)  # title方法可以獲取當前頁面的標題顯示的欄位
driver.find_element_by_xpath('').click()
driver.find_element_by_xpath('').send_keys('')
'''