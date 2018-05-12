from selenium import webdriver
import time
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://en.wikipedia.org")
print(driver.title)
time.sleep(10)
driver.quit()