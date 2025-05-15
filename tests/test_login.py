from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

driver = webdriver.Chrome(options=chrome_options)

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
