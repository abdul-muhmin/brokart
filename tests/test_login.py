from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Replace with your preferred browser driver
driver.get("https://practicetestautomation.com/practice-test-login/")

# Enter credentials
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")

# Click Login button
driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

# Verify success message
success_message = driver.find_element(By.TAG_NAME, "h4").text
assert success_message == "Logged In Successfully"

driver.quit()