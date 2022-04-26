import pickle
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://kktix.com/events/hellochiayi0522/registrations/new')

# 先卡住輸入帳密之後再按 enter 執行
input("Press any button.")
cookies = driver.get_cookies()
with open('db_cookie.pickle','wb') as f:
    pickle.dump(cookies,f)