'''
This version only for KKtix
Remember to set website URL and xpath
First time you should run once to save the cookie into db_cookie.pickle
'''
import pickle
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time

start = time.time()
driver = webdriver.Chrome()
driver.get('https://kktix.com')

# 第一次先把 cookie 存到 pickle檔
# input("Press any button.")
# cookies = driver.get_cookies()
# with open('db_cookie.pickle','wb') as f:
#     pickle.dump(cookies,f)

# 加載事先存好的 cookie
cookies = pickle.load(open('./db_cookie.pickle', 'rb'))
for cookie in cookies:
    driver.add_cookie(cookie)

# 網頁刷新
driver.refresh()

button = driver.find_element_by_xpath("//div[@id='ticket_449177']/div[1]/span[@class='ticket-quantity ng-scope']/button[2]")
button.click()
button.click()

checkbox = driver.find_element_by_xpath("//*[@id='person_agree_terms']")
checkbox.click()

nextstep_btn = driver.find_element_by_xpath("//*[@id='registrationsNewApp']/div/div[5]/div[5]/button")
nextstep_btn.click()

end = time.time()
print (end - start)