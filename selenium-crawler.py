from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.chrome_executable_path = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(options = options)
driver.get("https://www.google.com/")
driver.close()
