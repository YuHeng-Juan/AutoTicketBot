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
driver.get('https://kktix.com/events/hellochiayi0522/registrations/new')

# 加載事先存好的 cookie
try:
    cookies = pickle.load(open('./db_cookie.pickle', 'rb'))
    for cookie in cookies:
        driver.add_cookie(cookie)
except:
    print('Cookie file not exist!')

# 網頁刷新
driver.refresh()

button = driver.find_element_by_xpath("//div[@id='ticket_450819']/div[1]/span[@class='ticket-quantity ng-scope']/button[2]")
button.click()
button.click()

checkbox = driver.find_element_by_xpath("//*[@id='person_agree_terms']")
checkbox.click()

# 尚未售票時 button 會被隱藏起來，F12 就可以看到 button element，他只是被 disable 起來
nextstep_btn = driver.find_element_by_xpath("//*[@id='registrationsNewApp']/div/div[5]/div[4]/button") 
nextstep_btn.click()

end = time.time()
print (end - start)