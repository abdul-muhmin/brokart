from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up WebDriver
driver = webdriver.Chrome()  # Replace with your desired browser

# Navigate to the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Enter username and password
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")

# Click the Login button
driver.find_element(By.XPATH, "//button[text()='Login']").click()

# Verify success message
success_message = driver.find_element(By.TAG_NAME, "h1").text
assert success_message == "Logged In Successfully"

# Close the browser
driver.quit()