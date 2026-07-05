from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from login import login

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://tichi-app-webapp-stage.web.app/login")

login(driver, "", "")

input("Press Enter to close...")
driver.quit()