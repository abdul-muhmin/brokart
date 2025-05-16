import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    # Setup Chrome options
    options = Options()
    # Add any additional options here if needed (e.g., headless mode)
    # options.add_argument("--headless")

    # Initialize the Chrome driver
    service = Service()  # Uses the default ChromeDriver path
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)  # Implicit wait for elements to load
    yield driver
    driver.quit()


def test_login(driver):
    try:
        # 1. Navigate to the login page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # 2. Enter username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("student")

        # 3. Enter password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")

        # 4. Click the login button
        login_button = driver.find_element(By.ID, "submit")
        login_button.click()

        # 5. Verify successful login
        try:
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )
            assert success_message.text == "Logged In Successfully", f"Expected 'Logged In Successfully', but got '{success_message.text}'"
        except:
             assert False, "Login failed, success message not found."

    except Exception as e:
        pytest.fail(f"Test failed: {e}")
