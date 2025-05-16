from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configure Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Setup Chrome driver with Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # Step 1: Go to login page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Step 2: Fill in username and password
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("password123")

    # Step 3: Click Login
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)  # Let page load

    # Step 4: Verify success message
    success_text = driver.find_element(By.TAG_NAME, "h1").text
    assert success_text == "Logged In Successfully", "Login failed"

    print("✅ Test Passed")
except Exception as e:
    print("❌ Test Failed:", e)
    exit(1)
finally:
    driver.quit()
