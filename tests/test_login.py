from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Replace with your desired browser
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

assert "Logged In Successfully" in driver.page_source, "Login failed"

driver.quit()