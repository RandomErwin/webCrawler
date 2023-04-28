from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = Options()
options.chrome_executable_path = "/usr/local/bin/chromedriver"
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver = webdriver.Chrome(options = options)
driver.get("https://leetcode.com/accounts/login/")
usernameInput = driver.find_element(By.ID, "id_login")
passwordInput = driver.find_element(By.ID, "id_password")
usernameInput.send_keys("xxx@gmail.com")
passwordInput.send_keys("xxxxxx")
signinBtn = driver.find_element(By.ID, "signin_btn")
signinBtn.send_keys(Keys.ENTER)
time.sleep(15)

driver.get("https://leetcode.com/problemset/all/")
time.sleep(15)

statElement = driver.find_element(By.CSS_SELECTOR, "[data-difficulty = TOTAL]")

columns = statElement.text.split("\n")
print("已完成題目數量:", columns[1])

