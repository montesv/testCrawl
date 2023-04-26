# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
# import requests
# from bs4 import BeautifulSoup
#
# def getdata(url):
#     r = requests.get(url)
#     return r.text
#
# def soupscrape(site_url):
#
#     options = webdriver.ChromeOptions()
#     options.headless = True
#
#     options.page_load_strategy = 'none'
#
#     chrome_path = ChromeDriverManager().install()
#     chrome_service = Service(chrome_path)
#
#     driver = Chrome("/Users/vincentm/Downloads/chromedriver_mac64/chromedriver")
#     driver.implicitly_wait(5)
#
#     url = "https://www.redbubble.com/shop/?query=usf&ref=search_box/"
#
#     driver.get(url)
#     time.sleep(10)
#
#     # browser = webdriver.Chrome("/Users/vincentm/Downloads/chromedriver_mac64/chromedriver")
#     # browser.get("https://www.redbubble.com/shop/?query=usf&ref=search_box/")
#
#     # images = browser.find_elements_by_tag_name('img')
#
#     content = driver.find_element(By.CSS_SELECTOR, "img[src*='jpg']")
#
#
#     # htmldata = urlopen("https://www.redbubble.com/shop/?query=usf&ref=search_box/")
#     # htmldata = getdata("https://www.redbubble.com/shop/?query=usf&ref=search_box/")
#     # soup = BeautifulSoup(htmldata, 'html.parser')
#     # images = soup.find_all('img')
#
#     for item in content:
#             print(item.get_attribute('src'))