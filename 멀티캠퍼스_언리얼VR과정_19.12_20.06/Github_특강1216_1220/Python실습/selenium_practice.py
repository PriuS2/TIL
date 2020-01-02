from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = './chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.google.com/')

#검색창 선택
search_input = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

#검색할 내용 입력 + enter
search_input.send_keys('검색할 내용\n')

#return키(=enter) 입력
#search_input.send_keys(Keys.RETURN)
