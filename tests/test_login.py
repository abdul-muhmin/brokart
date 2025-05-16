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
    time.sleep(1)

    # Step 2: Fill in username and password
    driver.find_element(By.ID, "username").send_keys("student")        # valid username
    driver.find_element(By.ID, "password").send_keys("wrongpassword")  # try invalid password

    # Step 3: Click Login
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    # Step 4: Check for error message first
    error_elements = driver.find_elements(By.ID, "error")
    if error_elements:
        error_text = error_elements[0].text
        print(f"❌ Login failed. Error: '{error_text}'")
        assert "Your password is invalid!" in error_text or "Your username is invalid!" in error_text, \
            f"Unexpected error message: {error_text}"

    else:
        # No error message, check for success
        success_elements = driver.find_elements(By.TAG_NAME, "h1")
        if success_elements:
            success_text = success_elements[0].text
            assert success_text == "Logged In Successfully", \
                f"Unexpected success message: {success_text}"
            print("Login successful!")
        else:
            # Neither error nor success message found
            raise AssertionError("Login result unclear: no success or error message found.")

except AssertionError as ae:
    print("Test Failed:", ae)
    exit(1)

except Exception as e:
    print("Unexpected error during test:", e)
    exit(1)

finally:
    driver.quit()
