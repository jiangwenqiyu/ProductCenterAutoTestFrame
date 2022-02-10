from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.binary_location = r'D:\百分浏览器\CentBrowser\Application\chrome.exe'


browser = webdriver.Chrome(r'F:\Python3\chromedriver.exe', options = options)

url = 'http://product.xinfangsheng.com/finance/priceManage/chageFromManageSellPrice'
browser.get(url)
time.sleep(2)
cook = {'name':'uc_token',
        'value':'cb3bac116e7c4b70b793e1d38340d6c0',
        'domain':'xinfangsheng.com'}
time.sleep(2)
browser.add_cookie(cook)
time.sleep(2)
browser.get(url)
















