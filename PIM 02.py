"""Test case ID:TC_PIM_02"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\Users\\User\\Downloads\\chromedriver_win32(1)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)
username = driver.find_element(By.XPATH,'//input[@name="username"]').send_keys('Admin')
password = driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('admin123')
login_button = driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(10)
pim_module=driver.find_element(By.XPATH,'//a[@href="/web/index.php/pim/viewPimModule"]').click()
time.sleep(10)
Employee_name=driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("Alice Duval")
time.sleep(5)
Search= driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()
time.sleep(5)
Edit= driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-pencil-fill']").click()
time.sleep(5)
first_name =driver.find_element(By.XPATH,'//input[@placeholder="First Name"]')
first_name.send_keys(Keys.CONTROL + 'a')
first_name.send_keys(Keys.DELETE)
first_name.send_keys("Aliya")
time.sleep(5)
last_name =driver.find_element(By.XPATH,'//input[@name="lastName"]')
last_name.send_keys(Keys.CONTROL + 'a')
last_name.send_keys(Keys.DELETE)
last_name.send_keys("Bhatt")
time.sleep(5)
Save=driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()
time.sleep(5)
success_message = driver.find_element(By.ID,"oxd-toaster_1")
success_message_text=success_message.text
print("Successfully Saved",success_message_text)
driver.quit()