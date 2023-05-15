"""Test case ID:TC_Login_02"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\\Users\\User\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)
username = driver.find_element(By.XPATH,'//input[@name="username"]').send_keys('Admin')
password = driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('admin1234')
login_button=driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(5)
error_message = driver.find_element(By.XPATH,'//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')
error_message_text = error_message.text
print("Error Message:", error_message_text)
driver.quit()


